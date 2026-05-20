# COPY_BATCH_001 Analysis Report

- Analyzer: AXIS-Cosmos COPY_BATCH_001 read-only analyzer skeleton
- Version: 0.4.0
- Run ID: 2026-05-20T11:42:06.194117+00:00
- Root: `/home/sanghop/axis/axis-cosmos-lab`

## Derived / Non-Canonical Banner

This analysis is derived from COPY_BATCH_001 rescue fixtures. It is not Canon, not an authoritative AXIS-Cosmos graph, and not a replacement for CSL, identity records, lineage records, or future validated graph outputs.

## Summary

- PASS: 6
- WARN: 2
- FAIL: 0

Status counts above are separate from consistency observations listed below.

## Per-File Overview

| Label | Status | Extension | Size | Shape Summary |
|---|---|---:|---:|---|
| `graph_schema` | `PASS` | `.json` | `2706` | json dict; 10 keys; clusters=2 |
| `cosmos_graph` | `PASS` | `.json` | `7267` | json dict; 8 keys; nodes=11; edges=21; clusters=3 |
| `cosmos_paths` | `PASS` | `.json` | `2503` | json dict; 3 keys; paths=3 |
| `metrics_csv` | `WARN` | `.csv` | `28115` | csv 4 columns; rows=747; first headers: PD#PN, PageRank, InDegree, OutDegree |
| `edges_csv` | `WARN` | `.csv` | `151527` | csv 2 columns; rows=7217; first headers: Source, Target |
| `connection_report` | `PASS` | `.md` | `3277` | markdown lines=67; derived wording=not_detected |
| `provenance` | `PASS` | `.md` | `4425` | markdown lines=23; derived wording=present |
| `validation_reports` | `PASS` | `n/a` | `n/a` | markdown reports=5; names: COPY_BATCH_001_VALIDATION_REPORT.md, PHASE_002_AUTONOMOUS_AUDIT_VALIDATION_REPORT.md, PHASE_002_BATCH_002_VALIDATION_REPORT.md, PUBLIC_RELEASE_VALIDATION_REPORT.md, README.md |

## Shallow Consistency Checks

- `graph_schema`:
  - json_top_level_ok=True
  - json_nonempty_object=True
- `cosmos_graph`:
  - json_top_level_ok=True
  - json_nonempty_object=True
- `cosmos_paths`:
  - json_top_level_ok=True
  - json_nonempty_object=True
- `metrics_csv`:
  - csv_header_nonempty=True
  - csv_has_data_rows=True
- `edges_csv`:
  - csv_header_nonempty=True
  - csv_has_data_rows=True
- `connection_report`:
  - markdown_nonempty=True
  - derived_wording_detected=not_detected
- `provenance`:
  - markdown_nonempty=True
  - derived_wording_detected=present
- `validation_reports`:
  - validation_reports_present=true

Inventory output is available when this analyzer is run with `--inventory`: `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`.

## Findings

### graph_schema

- Path: `/home/sanghop/axis/axis-cosmos-lab/cosmos/schemas/graph_schema.json`
- Status: `PASS`

Facts:
- present=true
- file_size=2706
- extension=.json
- json_top_level_type=dict
- json_key_count=10
- json_keys=clusters, compatibility, description, edge, engine, invariant, node, relation_types, schema, version
- clusters_count=2

### cosmos_graph

- Path: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_graph.json`
- Status: `PASS`

Facts:
- present=true
- file_size=7267
- extension=.json
- json_top_level_type=dict
- json_key_count=8
- json_keys=clusters, edges, engine, generated, invariant, nodes, schema, stats
- nodes_count=11
- edges_count=21
- clusters_count=3

### cosmos_paths

- Path: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_paths.json`
- Status: `PASS`

Facts:
- present=true
- file_size=2503
- extension=.json
- json_top_level_type=dict
- json_key_count=3
- json_keys=generated, paths, schema
- paths_count=3

### metrics_csv

- Path: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Metricas.csv`
- Status: `WARN`

Facts:
- present=true
- file_size=28115
- extension=.csv
- csv_delimiter=';'
- csv_delimiter_detection=sniffer
- csv_header_columns=4
- csv_header_first5=PD#PN, PageRank, InDegree, OutDegree
- csv_data_rows=747

Warnings:
- SQL-derived archaeology context; non-canonical until rewritten from CSL/static indexes

### edges_csv

- Path: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- Status: `WARN`

Facts:
- present=true
- file_size=151527
- extension=.csv
- csv_delimiter=';'
- csv_delimiter_detection=sniffer
- csv_header_columns=2
- csv_header_first5=Source, Target
- csv_data_rows=7217

Warnings:
- SQL-derived archaeology context; non-canonical until rewritten from CSL/static indexes

### connection_report

- Path: `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/Grafo_Conexoes_Report.md`
- Status: `PASS`

Facts:
- present=true
- file_size=3277
- extension=.md
- markdown_lines=67
- derived_non_canonical_wording=not_detected

### provenance

- Path: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`
- Status: `PASS`

Facts:
- present=true
- file_size=4425
- extension=.md
- markdown_lines=23
- derived_non_canonical_wording=present

### validation_reports

- Path: `/home/sanghop/axis/axis-cosmos-lab/outputs/validation`
- Status: `PASS`

Facts:
- validation_report_count=5
- validation_report_names=COPY_BATCH_001_VALIDATION_REPORT.md, PHASE_002_AUTONOMOUS_AUDIT_VALIDATION_REPORT.md, PHASE_002_BATCH_002_VALIDATION_REPORT.md, PUBLIC_RELEASE_VALIDATION_REPORT.md, README.md

## Safety Confirmation

- Fixtures/artifacts modified: no.
- Production touched: no.
- Published touched: no.
- Git initialized: no.
- Builds, pipelines, provider/API/LLM calls: no.
- Network calls: no.
