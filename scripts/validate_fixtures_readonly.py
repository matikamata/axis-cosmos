#!/usr/bin/env python3
"""Read-only validator for AXIS-Cosmos COPY_BATCH_001 fixtures."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


VALIDATOR_NAME = "AXIS-Cosmos COPY_BATCH_001 read-only fixture validator"
VALIDATOR_VERSION = "0.1.1"

EXPECTED_ROOT_NAME = "axis-cosmos-lab"

FORBIDDEN_PATTERNS = [
    "tenweb_backup_db.sql",
    "wp-config.php",
    "DB_PASSWORD",
    "GOOGLE_APPLICATION_CREDENTIALS",
    "DEEPL",
    "API_KEY",
    "SECRET",
    "TOKEN",
    "/home/sanghop/",
    "/media/sanghop/",
    ".git/",
    ".venv",
    ".netlify",
    "node_modules",
    "__pycache__",
    "._",
]

CREDENTIAL_PATTERNS = {
    "DB_PASSWORD",
    "GOOGLE_APPLICATION_CREDENTIALS",
    "DEEPL",
    "API_KEY",
    "SECRET",
    "TOKEN",
}

LOCAL_PATH_PATTERNS = {"/home/sanghop/", "/media/sanghop/"}

TARGETS = {
    "graph_schema": Path("cosmos/schemas/graph_schema.json"),
    "cosmos_graph": Path("fixtures/zibaldone/cosmos_graph.json"),
    "cosmos_paths": Path("fixtures/zibaldone/cosmos_paths.json"),
    "metrics_csv": Path("fixtures/zibaldone/Grafo_Metricas.csv"),
    "edges_csv": Path("fixtures/zibaldone/Grafo_Conexoes_PDPN.csv"),
    "report_md": Path("docs/rescue-20260520/Grafo_Conexoes_Report.md"),
    "provenance_md": Path("fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md"),
}

EXPECTED_JSON_KEYS = {
    "graph_schema": {"schema", "version", "engine", "node", "edge", "relation_types", "clusters", "compatibility"},
    "cosmos_graph": {"schema", "generated", "engine", "nodes", "edges", "clusters", "stats"},
    "cosmos_paths": {"schema", "generated", "paths"},
}

SEVERITY_ORDER = {"PASS": 0, "WARN": 1, "FAIL": 2, "BLOCKED": 3}


@dataclass
class FileResult:
    label: str
    path: Path
    checks: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    blocked: list[str] = field(default_factory=list)

    def status(self) -> str:
        if self.blocked:
            return "BLOCKED"
        if self.failures:
            return "FAIL"
        if self.warnings:
            return "WARN"
        return "PASS"

    def add(self, status: str, message: str) -> None:
        if status == "PASS":
            self.checks.append(message)
        elif status == "WARN":
            self.warnings.append(message)
        elif status == "FAIL":
            self.failures.append(message)
        elif status == "BLOCKED":
            self.blocked.append(message)
        else:
            self.failures.append(f"Unknown status {status}: {message}")


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent)
        return True
    except ValueError:
        return False


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    lowered = text.lower()
    return re.sub(r"[^a-z0-9]+", " ", lowered).strip()


def contains_marker(normalized_text: str, marker: str) -> bool:
    marker_norm = normalize_text(marker)
    return marker_norm in normalized_text


def protected_paths(root: Path) -> tuple[Path, Path]:
    parent = root.parent.resolve()
    return (parent / "axis-niddhi-production").resolve(), (parent / "axis-niddhi-published").resolve()


def scan_forbidden(result: FileResult, text: str, *, allow_local_paths: bool) -> None:
    for pattern in FORBIDDEN_PATTERNS:
        if pattern not in text:
            continue
        if pattern in LOCAL_PATH_PATTERNS and allow_local_paths:
            result.add("WARN", f"CONTEXT: local path pattern appears only in documentation/provenance context: {pattern}")
        elif pattern in CREDENTIAL_PATTERNS or pattern == "tenweb_backup_db.sql":
            result.add("FAIL", f"Forbidden credential/raw-source pattern found: {pattern}")
        elif pattern in LOCAL_PATH_PATTERNS:
            result.add("FAIL", f"Local private path found in fixture content: {pattern}")
        else:
            result.add("FAIL", f"Forbidden pattern found: {pattern}")
    result.add("PASS", "Forbidden-pattern scan completed")


def validate_path_safety(root: Path, report: Path | None) -> list[FileResult]:
    result = FileResult("path_safety", root)
    production, published = protected_paths(root)
    if root.name != EXPECTED_ROOT_NAME:
        result.add("BLOCKED", f"Root directory must be named {EXPECTED_ROOT_NAME}; got {root.name}")
        return [result]
    if root == production or root == published or is_relative_to(root, production) or is_relative_to(root, published):
        result.add("BLOCKED", "Root points into a protected production/published path")
        return [result]
    result.add("PASS", f"Root path accepted: {root}")

    for label, rel in TARGETS.items():
        target = (root / rel).resolve()
        if not is_relative_to(target, root):
            result.add("BLOCKED", f"{label} resolves outside lab root: {target}")
        if is_relative_to(target, production) or is_relative_to(target, published):
            result.add("BLOCKED", f"{label} resolves into protected path: {target}")
        if not target.exists():
            result.add("BLOCKED", f"Required target missing: {target}")
    if not result.blocked:
        result.add("PASS", "All target paths exist inside the lab and outside protected paths")

    if report is not None:
        expected_report_root = (root / "outputs/validation").resolve()
        if not is_relative_to(report, expected_report_root):
            result.add("BLOCKED", f"Report path must be inside {expected_report_root}; got {report}")
        else:
            result.add("PASS", "Report path is inside outputs/validation")
    return [result]


def validate_json(root: Path, label: str, rel: Path) -> FileResult:
    path = (root / rel).resolve()
    result = FileResult(label, path)
    text = read_text(path)
    scan_forbidden(result, text, allow_local_paths=False)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        result.add("FAIL", f"JSON parse failed: {exc}")
        return result
    result.add("PASS", "JSON parse succeeded")
    if not isinstance(data, dict):
        result.add("FAIL", f"Top-level JSON type must be object; got {type(data).__name__}")
        return result
    result.add("PASS", f"Top-level JSON type: object; keys: {', '.join(sorted(data.keys()))}")
    expected = EXPECTED_JSON_KEYS[label]
    missing = sorted(expected - set(data.keys()))
    if missing:
        result.add("FAIL", f"Missing expected top-level keys: {', '.join(missing)}")
    else:
        result.add("PASS", "Expected top-level keys present")

    if label == "graph_schema":
        if data.get("schema"):
            result.add("PASS", f"Schema identity present: {data.get('schema')}")
        else:
            result.add("WARN", "Schema identity missing")
    elif label == "cosmos_graph":
        nodes = data.get("nodes")
        edges = data.get("edges")
        if isinstance(nodes, list) and nodes:
            node_ids = {node.get("concept_id") for node in nodes if isinstance(node, dict)}
            missing_ids = [idx for idx, node in enumerate(nodes) if not isinstance(node, dict) or not node.get("concept_id")]
            if missing_ids:
                result.add("FAIL", f"Nodes missing concept_id at indexes: {missing_ids[:10]}")
            else:
                result.add("PASS", f"Concept nodes present: {len(nodes)}")
        else:
            node_ids = set()
            result.add("FAIL", "nodes must be a non-empty list")
        if isinstance(edges, list):
            unresolved = []
            for idx, edge in enumerate(edges):
                if not isinstance(edge, dict) or not edge.get("source") or not edge.get("target"):
                    unresolved.append(idx)
                    continue
                if node_ids and (edge["source"] not in node_ids or edge["target"] not in node_ids):
                    unresolved.append(idx)
            if unresolved:
                result.add("WARN", f"Edges with missing/unresolved source or target: {unresolved[:10]}")
            else:
                result.add("PASS", f"Edges reference known concept nodes: {len(edges)}")
        else:
            result.add("FAIL", "edges must be a list")
    elif label == "cosmos_paths":
        paths = data.get("paths")
        if isinstance(paths, dict) and paths:
            result.add("PASS", f"Named paths present: {len(paths)}")
        else:
            result.add("FAIL", "paths must be a non-empty object")
    return result


def detect_delimiter(header: str) -> str:
    if ";" in header:
        return ";"
    if "," in header:
        return ","
    return ""


def validate_csv(root: Path, label: str, rel: Path) -> FileResult:
    path = (root / rel).resolve()
    result = FileResult(label, path)
    text = read_text(path)
    scan_forbidden(result, text, allow_local_paths=False)
    lines = text.splitlines()
    if not lines:
        result.add("FAIL", "CSV is empty")
        return result
    delimiter = detect_delimiter(lines[0])
    if delimiter != ";":
        result.add("FAIL", f"Expected semicolon delimiter; got {delimiter or 'unknown'}")
        return result
    result.add("PASS", "Semicolon delimiter detected")
    reader = csv.DictReader(lines, delimiter=delimiter)
    expected = ["PD#PN", "PageRank", "InDegree", "OutDegree"] if label == "metrics_csv" else ["Source", "Target"]
    if reader.fieldnames != expected:
        result.add("FAIL", f"Expected columns {expected}; got {reader.fieldnames}")
        return result
    result.add("PASS", f"Expected columns present: {', '.join(expected)}")
    row_count = 0
    empty_required = 0
    bad_numeric = 0
    for row in reader:
        row_count += 1
        if label == "edges_csv":
            if not row.get("Source") or not row.get("Target"):
                empty_required += 1
        else:
            if not row.get("PD#PN"):
                empty_required += 1
            for key in ("PageRank", "InDegree", "OutDegree"):
                try:
                    float(row.get(key, ""))
                except ValueError:
                    bad_numeric += 1
    result.add("PASS", f"Data row count: {row_count}")
    if empty_required:
        result.add("FAIL", f"Empty required cells found: {empty_required}")
    else:
        result.add("PASS", "No empty required cells found")
    if bad_numeric:
        result.add("FAIL", f"Metric numeric parse failures: {bad_numeric}")
    elif label == "metrics_csv":
        result.add("PASS", "Metric numeric fields parse successfully")
    result.add("WARN", "CONTEXT: SQL-derived archaeology fixture; structurally valid, but not canonical until rewritten from CSL/static indexes")
    return result


def validate_markdown(root: Path, label: str, rel: Path) -> FileResult:
    path = (root / rel).resolve()
    result = FileResult(label, path)
    text = read_text(path)
    scan_forbidden(result, text, allow_local_paths=True)
    if text.strip():
        result.add("PASS", "Markdown is non-empty UTF-8 text")
    else:
        result.add("FAIL", "Markdown is empty")
    normalized = normalize_text(text)
    marker_candidates = [
        "derived",
        "non canonical",
        "not canon",
        "not axis niddhi canon",
        "archaeology",
        "provenance",
    ]
    if any(contains_marker(normalized, marker) for marker in marker_candidates):
        result.add("PASS", "Derived/non-canonical status is mentioned")
    else:
        result.add("WARN", "CONTEXT: copied archaeology Markdown is readable, but its own body lacks an explicit derived/non-canonical label")
    return result


def validate_provenance(root: Path, provenance_result: FileResult) -> None:
    text = read_text(provenance_result.path)
    normalized = normalize_text(text)
    required = [
        ("source path", ["source path", "source"]),
        ("destination path", ["destination path", "destination"]),
        ("Source SHA-256", ["source sha 256", "source sha256"]),
        ("Copied SHA-256", ["copied sha 256", "copied sha256"]),
        ("Review note", ["review note", "review"]),
        ("Required label", ["required label", "label"]),
        ("COPY_BATCH_001 Report", ["copy batch 001 report", "batch 001 report"]),
    ]
    for display, variants in required:
        if any(contains_marker(normalized, variant) for variant in variants):
            provenance_result.add("PASS", f"Provenance marker present: {display}")
        else:
            provenance_result.add("WARN", f"CONTEXT: provenance marker not found via normalized matching, review formatting before relying on automation: {display}")
    for rel in TARGETS.values():
        if str(rel) in text or rel.name in text:
            provenance_result.add("PASS", f"Provenance references copied file: {rel}")
        else:
            provenance_result.add("WARN", f"CONTEXT: provenance may not reference this file explicitly; confirm whether this is self-reference or formatting drift: {rel}")


def render_report(root: Path, results: list[FileResult]) -> str:
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "BLOCKED": 0}
    for result in results:
        counts[result.status()] += 1
    timestamp = datetime.now(timezone.utc).isoformat()
    lines = [
        "# COPY_BATCH_001 Validation Report",
        "",
        f"- Validator: {VALIDATOR_NAME}",
        f"- Version: {VALIDATOR_VERSION}",
        f"- Run ID: {timestamp}",
        f"- Root: `{root}`",
        "",
        "## Summary",
        "",
        f"- PASS: {counts['PASS']}",
        f"- WARN: {counts['WARN']}",
        f"- FAIL: {counts['FAIL']}",
        f"- BLOCKED: {counts['BLOCKED']}",
        "",
        "WARN entries in this report are provenance/context warnings unless paired with FAIL or BLOCKED. They are non-blocking and do not indicate fixture mutation or validation failure.",
        "",
        "## Target Files Checked",
        "",
    ]
    for label, rel in TARGETS.items():
        lines.append(f"- `{label}`: `{rel}`")
    lines.extend(["", "## Per-File Results", ""])
    for result in results:
        lines.extend([
            f"### {result.label}",
            "",
            f"- File: `{result.path}`",
            f"- Status: `{result.status()}`",
            "",
        ])
        if result.checks:
            lines.append("Checks passed:")
            for item in result.checks:
                lines.append(f"- {item}")
            lines.append("")
        if result.warnings:
            lines.append("Warnings:")
            for item in result.warnings:
                lines.append(f"- {item}")
            lines.append("")
        if result.failures:
            lines.append("Failures:")
            for item in result.failures:
                lines.append(f"- {item}")
            lines.append("")
        if result.blocked:
            lines.append("Blocked:")
            for item in result.blocked:
                lines.append(f"- {item}")
            lines.append("")
    if counts["BLOCKED"] or counts["FAIL"]:
        action = "Review failures before any further migration or implementation."
    elif counts["WARN"]:
        action = "Review non-blocking provenance/context warnings, then proceed only with explicit operator acceptance."
    else:
        action = "All checks passed; next safe step is operator review of this report."
    lines.extend([
        "## Recommended Next Action",
        "",
        action,
        "",
        "## Do Not Touch Confirmation",
        "",
        "- Production touched: no.",
        "- Published touched: no.",
        "- Fixtures modified: no.",
        "- More Zibaldone files copied: no.",
        "- Git initialized: no.",
        "- Builds, pipelines, scripts, provider/API/LLM calls: no.",
        "- Commits, pushes, deploys: no.",
        "",
    ])
    return "\n".join(lines)


def run(root: Path, report: Path | None) -> tuple[int, str]:
    production, published = protected_paths(root)
    if report is not None:
        expected_report_root = (root / "outputs/validation").resolve()
        if not is_relative_to(report, expected_report_root):
            blocked = FileResult("path_safety", root)
            blocked.add("BLOCKED", f"Report path must be inside {expected_report_root}; got {report}")
            return 2, render_report(root, [blocked])
        if is_relative_to(report, production) or is_relative_to(report, published):
            blocked = FileResult("path_safety", root)
            blocked.add("BLOCKED", f"Report path resolves into protected path: {report}")
            return 2, render_report(root, [blocked])

    results = validate_path_safety(root, report)
    if any(result.status() == "BLOCKED" for result in results):
        output = render_report(root, results)
        return 2, output

    results.extend([
        validate_json(root, "graph_schema", TARGETS["graph_schema"]),
        validate_json(root, "cosmos_graph", TARGETS["cosmos_graph"]),
        validate_json(root, "cosmos_paths", TARGETS["cosmos_paths"]),
        validate_csv(root, "metrics_csv", TARGETS["metrics_csv"]),
        validate_csv(root, "edges_csv", TARGETS["edges_csv"]),
        validate_markdown(root, "report_md", TARGETS["report_md"]),
        validate_markdown(root, "provenance_md", TARGETS["provenance_md"]),
    ])
    provenance = next(result for result in results if result.label == "provenance_md")
    validate_provenance(root, provenance)
    output = render_report(root, results)
    if any(result.status() == "BLOCKED" for result in results):
        return 2, output
    if any(result.status() == "FAIL" for result in results):
        return 1, output
    return 0, output


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=VALIDATOR_NAME)
    parser.add_argument("--root", required=True, help="Absolute path to axis-cosmos-lab")
    parser.add_argument("--report", help="Optional explicit report path under outputs/validation")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).expanduser().resolve()
    report = Path(args.report).expanduser().resolve() if args.report else None
    status, output = run(root, report)
    production, published = protected_paths(root)
    if report is not None:
        expected_report_root = (root / "outputs/validation").resolve()
        if not is_relative_to(report, expected_report_root):
            raise SystemExit(f"Refusing report write outside {expected_report_root}: {report}")
        if is_relative_to(report, production) or is_relative_to(report, published):
            raise SystemExit(f"Refusing report write to protected path: {report}")
        report.write_text(output, encoding="utf-8")
    summary_lines = []
    for line in output.splitlines():
        if line.startswith("- PASS:") or line.startswith("- WARN:") or line.startswith("- FAIL:") or line.startswith("- BLOCKED:"):
            summary_lines.append(line)
    print("\n".join(summary_lines))
    if report is not None:
        print(f"Report: {report}")
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
