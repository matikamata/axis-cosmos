#!/usr/bin/env python3
"""Minimal read-only analyzer for AXIS-Cosmos COPY_BATCH_001 artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ANALYZER_NAME = "AXIS-Cosmos COPY_BATCH_001 read-only analyzer skeleton"
ANALYZER_VERSION = "0.4.0"
EXPECTED_ROOT_NAME = "axis-cosmos-lab"

DERIVED_LABEL = (
    "This analysis is derived from COPY_BATCH_001 rescue fixtures. "
    "It is not Canon, not an authoritative AXIS-Cosmos graph, and not a replacement "
    "for CSL, identity records, lineage records, or future validated graph outputs."
)

TARGETS = [
    ("graph_schema", Path("cosmos/schemas/graph_schema.json"), True),
    ("cosmos_graph", Path("fixtures/zibaldone/cosmos_graph.json"), True),
    ("cosmos_paths", Path("fixtures/zibaldone/cosmos_paths.json"), True),
    ("metrics_csv", Path("fixtures/zibaldone/Grafo_Metricas.csv"), True),
    ("edges_csv", Path("fixtures/zibaldone/Grafo_Conexoes_PDPN.csv"), True),
    ("connection_report", Path("docs/rescue-20260520/Grafo_Conexoes_Report.md"), True),
    ("provenance", Path("fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md"), True),
]

VALIDATION_DIR = Path("outputs/validation")


@dataclass
class Finding:
    label: str
    path: Path
    status: str
    facts: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    consistency: list[str] = field(default_factory=list)
    required: bool = True


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent)
        return True
    except ValueError:
        return False


def protected_paths(root: Path) -> tuple[Path, Path]:
    parent = root.parent.resolve()
    return (parent / "axis-niddhi-production").resolve(), (parent / "axis-niddhi-published").resolve()


def unsafe_path(path: Path, root: Path) -> bool:
    production, published = protected_paths(root)
    resolved = path.resolve()
    return is_relative_to(resolved, production) or is_relative_to(resolved, published)


def require_safe_root(root: Path) -> None:
    if root.name != EXPECTED_ROOT_NAME:
        raise ValueError(f"--root directory name must be {EXPECTED_ROOT_NAME}; got {root.name}")
    if "axis-niddhi-production" in root.parts or "axis-niddhi-published" in root.parts:
        raise ValueError("--root resolves inside a protected path")
    if unsafe_path(root, root):
        raise ValueError("--root resolves inside production/published")


def require_safe_report(report: Path) -> None:
    # We still enforce target under <root>/outputs/analysis at call sites; this function validates safety and scope.
    if "outputs/analysis" not in str(report):
        raise ValueError("report path must include outputs/analysis")
    root = report
    while root.name and root.name != EXPECTED_ROOT_NAME:
        root = root.parent
    if root.name != EXPECTED_ROOT_NAME:
        raise ValueError(f"Unable to infer {EXPECTED_ROOT_NAME} from report path: {report}")
    expected = (root / "outputs/analysis").resolve()
    if not is_relative_to(report, expected):
        raise ValueError(f"--report must resolve under {expected}; got {report}")
    if unsafe_path(report, root):
        raise ValueError("--report resolves inside production/published")


def detect_csv_dialect(sample: str) -> tuple[str, str]:
    preferred = [";", ",", "\t"]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=";,\t")
        delimiter = dialect.delimiter
        if delimiter in preferred:
            return delimiter, "sniffer"
    except csv.Error:
        pass
    lines = [line for line in sample.splitlines() if line.strip()]
    header = lines[0] if lines else ""
    counts = {d: header.count(d) for d in preferred}
    best = max(preferred, key=lambda d: counts[d])
    if counts[best] > 0:
        return best, "fallback_header_count"
    return ";", "fallback_default"


def parse_json(path: Path) -> tuple[list[str], list[str]]:
    facts: list[str] = []
    warnings: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        data: Any = json.load(handle)
    top_type = type(data).__name__
    facts.append(f"json_top_level_type={top_type}")
    if top_type not in {"dict", "list"}:
        raise ValueError(f"JSON top-level must be object or list; got {top_type}")
    if isinstance(data, dict):
        keys = sorted(str(key) for key in data.keys())
        facts.append(f"json_key_count={len(keys)}")
        facts.append("json_keys=" + ", ".join(keys))
        if len(keys) == 0:
            raise ValueError("JSON object must have at least one key")
        for key in ("nodes", "edges", "links", "paths", "clusters"):
            value = data.get(key)
            if isinstance(value, (list, dict)):
                facts.append(f"{key}_count={len(value)}")
    elif isinstance(data, list):
        facts.append(f"json_items={len(data)}")
        if len(data) == 0:
            raise ValueError("JSON list must have at least one item")
    return facts, warnings


def parse_csv(path: Path) -> tuple[list[str], list[str]]:
    facts: list[str] = []
    warnings: list[str] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        delimiter, method = detect_csv_dialect(sample)
        reader = csv.reader(handle, delimiter=delimiter)
        header = next(reader, [])
        row_count = sum(1 for _ in reader)
    if not header:
        raise ValueError("CSV header is empty")
    if any(col.strip() == "" for col in header):
        raise ValueError("CSV header contains empty column names")
    if row_count < 1:
        raise ValueError("CSV must contain at least one data row")
    facts.append(f"csv_delimiter={repr(delimiter)}")
    facts.append(f"csv_delimiter_detection={method}")
    facts.append(f"csv_header_columns={len(header)}")
    facts.append("csv_header_first5=" + ", ".join(header[:5]))
    facts.append(f"csv_data_rows={row_count}")
    if "Grafo_" in path.name:
        warnings.append("SQL-derived archaeology context; non-canonical until rewritten from CSL/static indexes")
    return facts, warnings


def parse_markdown(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("Markdown file is empty")
    lower = text.lower()
    facts = [f"markdown_lines={len(text.splitlines())}"]
    if "derived" in lower or "non-canonical" in lower or "not canon" in lower:
        facts.append("derived_non_canonical_wording=present")
    else:
        facts.append("derived_non_canonical_wording=not_detected")
    return facts, []


def inspect_file(root: Path, label: str, rel: Path, required: bool) -> Finding:
    path = (root / rel).resolve()
    if not is_relative_to(path, root):
        raise ValueError(f"Forbidden path outside root: {path}")
    if unsafe_path(path, root):
        raise ValueError(f"Forbidden protected path: {path}")
    if not path.exists():
        status = "WARN" if not required else "FAIL"
        return Finding(label, path, status, warnings=[f"missing required={required}"], required=required)
    facts = [
        "present=true",
        f"file_size={path.stat().st_size}",
        f"extension={path.suffix or '(none)'}",
    ]
    warnings: list[str] = []
    try:
        if path.suffix == ".json":
            parsed_facts, parsed_warnings = parse_json(path)
        elif path.suffix == ".csv":
            parsed_facts, parsed_warnings = parse_csv(path)
        elif path.suffix == ".md":
            parsed_facts, parsed_warnings = parse_markdown(path)
        else:
            parsed_facts, parsed_warnings = (["parse_status=not_applicable"], [])
    except Exception as exc:
        raise ValueError(f"Parse failure for {path}: {exc}") from exc
    facts.extend(parsed_facts)
    warnings.extend(parsed_warnings)

    consistency: list[str] = []
    if path.suffix == ".json":
        top = next((fact.split("=", 1)[1] for fact in facts if fact.startswith("json_top_level_type=")), "unknown")
        consistency.append(f"json_top_level_ok={top in {'dict', 'list'}}")
        if top == "dict":
            key_count = int(next((fact.split("=", 1)[1] for fact in facts if fact.startswith("json_key_count=")), "0"))
            consistency.append(f"json_nonempty_object={key_count > 0}")
        elif top == "list":
            items = int(next((fact.split("=", 1)[1] for fact in facts if fact.startswith("json_items=")), "0"))
            consistency.append(f"json_nonempty_list={items > 0}")
    elif path.suffix == ".csv":
        cols = int(next((fact.split("=", 1)[1] for fact in facts if fact.startswith("csv_header_columns=")), "0"))
        rows = int(next((fact.split("=", 1)[1] for fact in facts if fact.startswith("csv_data_rows=")), "0"))
        consistency.append(f"csv_header_nonempty={cols > 0}")
        consistency.append(f"csv_has_data_rows={rows > 0}")
    elif path.suffix == ".md":
        lines = int(next((fact.split("=", 1)[1] for fact in facts if fact.startswith("markdown_lines=")), "0"))
        consistency.append(f"markdown_nonempty={lines > 0}")
        derived = next((fact.split("=", 1)[1] for fact in facts if fact.startswith("derived_non_canonical_wording=")), "not_detected")
        if label == "provenance" and derived != "present":
            warnings.append("Derived/non-canonical wording expected in provenance Markdown but not detected")
        consistency.append(f"derived_wording_detected={derived}")

    return Finding(label, path, "WARN" if warnings else "PASS", facts, warnings, consistency, required=required)


def inspect_validation_reports(root: Path) -> list[Finding]:
    directory = (root / VALIDATION_DIR).resolve()
    if not directory.exists():
        return [Finding("validation_reports", directory, "WARN", warnings=["outputs/validation missing"], required=False)]
    if not is_relative_to(directory, root) or unsafe_path(directory, root):
        raise ValueError(f"Forbidden validation report directory: {directory}")
    reports = sorted(directory.glob("*.md"))
    facts = [f"validation_report_count={len(reports)}"]
    facts.append("validation_report_names=" + ", ".join(report.name for report in reports))
    if len(reports) == 0:
        return [Finding("validation_reports", directory, "FAIL", facts=facts, consistency=["validation_reports_present=false"], required=False)]
    return [Finding("validation_reports", directory, "PASS", facts=facts, consistency=["validation_reports_present=true"], required=False)]


def run_analysis(root: Path) -> list[Finding]:
    require_safe_root(root)
    findings = [inspect_file(root, label, rel, required) for label, rel, required in TARGETS]
    findings.extend(inspect_validation_reports(root))
    return findings


def artifact_kind(path: Path) -> str:
    if path.is_dir():
        return "directory"
    suffix = path.suffix.lower()
    if suffix == ".json":
        return "JSON"
    if suffix == ".csv":
        return "CSV"
    if suffix == ".md":
        return "Markdown"
    return suffix or "unknown"


def parse_status_from_facts(facts: dict[str, str], status: str) -> str:
    if status == "FAIL":
        return "parse_failed_or_missing"
    if "json_top_level_type" in facts:
        return f"json_ok:{facts['json_top_level_type']}"
    if "csv_header_columns" in facts and "csv_data_rows" in facts:
        return f"csv_ok:cols={facts['csv_header_columns']},rows={facts['csv_data_rows']}"
    if "markdown_lines" in facts:
        return f"markdown_ok:lines={facts['markdown_lines']}"
    if "validation_report_count" in facts:
        return f"directory_ok:reports={facts['validation_report_count']}"
    return "n/a"


def consistency_status(finding: Finding) -> str:
    if finding.status == "FAIL":
        return "failed"
    if finding.status == "WARN":
        return "warn"
    if finding.consistency:
        return "ok"
    return "n/a"


def provenance_class_for(label: str) -> str:
    if label in {"graph_schema", "cosmos_graph", "cosmos_paths", "metrics_csv", "edges_csv"}:
        return "copied_rescue_fixture"
    if label == "connection_report":
        return "derived_archaeology_context"
    if label == "provenance":
        return "rescue_documentation"
    if label == "validation_reports":
        return "validation_report"
    return "rescue_documentation"


def canonical_status_for(label: str) -> str:
    if label in {"graph_schema", "cosmos_graph", "cosmos_paths", "metrics_csv", "edges_csv", "connection_report"}:
        return "derived_non_canonical"
    if label == "validation_reports":
        return "validation_context_only"
    return "non_canonical"


def allowed_future_use_for(label: str) -> str:
    if label in {"graph_schema", "cosmos_graph", "cosmos_paths", "metrics_csv", "edges_csv"}:
        return "inspect_shape_only; compare_against_future_csl_derived_output; do_not_treat_as_authority"
    if label == "connection_report":
        return "operator_context_only; do_not_treat_as_authority"
    if label == "provenance":
        return "operator_context_only"
    if label == "validation_reports":
        return "operator_context_only"
    return "do_not_treat_as_authority"


def render_inventory(root: Path, findings: list[Finding]) -> str:
    lines = [
        "# COPY_BATCH_001 Fixture Inventory",
        "",
        "This inventory is an index of COPY_BATCH_001 rescue artifacts. It is not a graph, not Canon, not a Navigator export, and not an authoritative source of truth.",
        "",
        f"- Root: `{root}`",
        f"- Generated by: {ANALYZER_NAME} v{ANALYZER_VERSION}",
        "",
        "| Relative path | Artifact kind | Present | Size | Parse status | Shallow consistency status | Provenance class | Canonical status | Allowed future use |",
        "|---|---|---|---:|---|---|---|---|---|",
    ]
    for finding in findings:
        facts = dict(fact.split("=", 1) for fact in finding.facts if "=" in fact)
        rel = str(finding.path.relative_to(root)) if is_relative_to(finding.path, root) else str(finding.path)
        present = "yes" if finding.path.exists() else "no"
        size = facts.get("file_size", "n/a")
        parse_status = parse_status_from_facts(facts, finding.status)
        shallow = consistency_status(finding)
        prov = provenance_class_for(finding.label)
        canon = canonical_status_for(finding.label)
        use = allowed_future_use_for(finding.label)
        lines.append(
            f"| `{rel}` | `{artifact_kind(finding.path)}` | `{present}` | `{size}` | `{parse_status}` | `{shallow}` | `{prov}` | `{canon}` | `{use}` |"
        )
    lines.extend([
        "",
        "## Safety Confirmation",
        "",
        "- Fixtures/artifacts modified: no.",
        "- `Grafo_Conexoes_Report.md` edited: no.",
        "- Production touched: no.",
        "- Published touched: no.",
        "- Git initialized: no.",
        "- Builds, pipelines, provider/API/LLM/network calls: no.",
        "",
    ])
    return "\n".join(lines)


def render_report(root: Path, findings: list[Finding]) -> str:
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for finding in findings:
        counts[finding.status] = counts.get(finding.status, 0) + 1
    lines = [
        "# COPY_BATCH_001 Analysis Report",
        "",
        f"- Analyzer: {ANALYZER_NAME}",
        f"- Version: {ANALYZER_VERSION}",
        f"- Run ID: {datetime.now(timezone.utc).isoformat()}",
        f"- Root: `{root}`",
        "",
        "## Derived / Non-Canonical Banner",
        "",
        DERIVED_LABEL,
        "",
        "## Summary",
        "",
        f"- PASS: {counts.get('PASS', 0)}",
        f"- WARN: {counts.get('WARN', 0)}",
        f"- FAIL: {counts.get('FAIL', 0)}",
        "",
        "Status counts above are separate from consistency observations listed below.",
        "",
        "## Per-File Overview",
        "",
        "| Label | Status | Extension | Size | Shape Summary |",
        "|---|---|---:|---:|---|",
    ]
    for finding in findings:
        facts = dict(fact.split("=", 1) for fact in finding.facts if "=" in fact)
        extension = facts.get("extension", "n/a")
        size = facts.get("file_size", "n/a")
        if "json_top_level_type" in facts:
            shape_parts = [f"json {facts['json_top_level_type']}"]
            if "json_key_count" in facts:
                shape_parts.append(f"{facts['json_key_count']} keys")
            for key in ("nodes_count", "edges_count", "links_count", "paths_count", "clusters_count", "json_items"):
                if key in facts:
                    shape_parts.append(f"{key.replace('_count', '')}={facts[key]}")
            shape = "; ".join(shape_parts)
        elif "csv_header_columns" in facts:
            shape = f"csv {facts.get('csv_header_columns')} columns; rows={facts.get('csv_data_rows', 'n/a')}; first headers: {facts.get('csv_header_first5', '')}"
        elif "markdown_lines" in facts:
            shape = f"markdown lines={facts.get('markdown_lines')}; derived wording={facts.get('derived_non_canonical_wording', 'unknown')}"
        elif "validation_report_count" in facts:
            shape = f"markdown reports={facts.get('validation_report_count')}; names: {facts.get('validation_report_names', '')}"
        else:
            shape = "n/a"
        lines.append(f"| `{finding.label}` | `{finding.status}` | `{extension}` | `{size}` | {shape} |")
    lines.extend([
        "",
        "## Shallow Consistency Checks",
        "",
    ])
    for finding in findings:
        if not finding.consistency:
            continue
        lines.append(f"- `{finding.label}`:")
        for item in finding.consistency:
            lines.append(f"  - {item}")
    lines.extend([
        "",
        "Inventory output is available when this analyzer is run with `--inventory`: `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`.",
        "",
        "## Findings",
        "",
    ])
    for finding in findings:
        lines.extend([
            f"### {finding.label}",
            "",
            f"- Path: `{finding.path}`",
            f"- Status: `{finding.status}`",
            "",
        ])
        if finding.facts:
            lines.append("Facts:")
            lines.extend(f"- {fact}" for fact in finding.facts)
            lines.append("")
        if finding.warnings:
            lines.append("Warnings:")
            lines.extend(f"- {warning}" for warning in finding.warnings)
            lines.append("")
    lines.extend([
        "## Safety Confirmation",
        "",
        "- Fixtures/artifacts modified: no.",
        "- Production touched: no.",
        "- Published touched: no.",
        "- Git initialized: no.",
        "- Builds, pipelines, provider/API/LLM calls: no.",
        "- Network calls: no.",
        "",
    ])
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=ANALYZER_NAME)
    parser.add_argument("--root", required=True)
    parser.add_argument("--report")
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--inventory-path")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).expanduser().resolve()
    report = Path(args.report).expanduser().resolve() if args.report else None
    default_inventory = (root / "outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md").resolve()
    inventory_path = Path(args.inventory_path).expanduser().resolve() if args.inventory_path else default_inventory
    if report is not None:
        require_safe_report(report)
    if args.inventory:
        require_safe_report(inventory_path)
    findings = run_analysis(root)
    output = render_report(root, findings)
    if report is not None:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(output, encoding="utf-8")
    if args.inventory:
        inventory_text = render_inventory(root, findings)
        inventory_path.parent.mkdir(parents=True, exist_ok=True)
        inventory_path.write_text(inventory_text, encoding="utf-8")
    summary = []
    for line in output.splitlines():
        if line.startswith("- PASS:") or line.startswith("- WARN:") or line.startswith("- FAIL:"):
            summary.append(line)
    print("\n".join(summary))
    if report is not None:
        print(f"Report: {report}")
    return 1 if any(finding.status == "FAIL" for finding in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
