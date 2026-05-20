# COPY_BATCH_001 Validation Report

- Validator: AXIS-Cosmos COPY_BATCH_001 read-only fixture validator
- Version: 0.1.1
- Run ID: 2026-05-20T11:42:06.160762+00:00
- Root: `/home/sanghop/axis/axis-cosmos-lab`

## Summary

- PASS: 4
- WARN: 4
- FAIL: 0
- BLOCKED: 0

WARN entries in this report are provenance/context warnings unless paired with FAIL or BLOCKED. They are non-blocking and do not indicate fixture mutation or validation failure.

## Target Files Checked

- `graph_schema`: `cosmos/schemas/graph_schema.json`
- `cosmos_graph`: `fixtures/zibaldone/cosmos_graph.json`
- `cosmos_paths`: `fixtures/zibaldone/cosmos_paths.json`
- `metrics_csv`: `fixtures/zibaldone/Grafo_Metricas.csv`
- `edges_csv`: `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- `report_md`: `docs/rescue-20260520/Grafo_Conexoes_Report.md`
- `provenance_md`: `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`

## Per-File Results

### path_safety

- File: `/home/sanghop/axis/axis-cosmos-lab`
- Status: `PASS`

Checks passed:
- Root path accepted: /home/sanghop/axis/axis-cosmos-lab
- All target paths exist inside the lab and outside protected paths
- Report path is inside outputs/validation

### graph_schema

- File: `/home/sanghop/axis/axis-cosmos-lab/cosmos/schemas/graph_schema.json`
- Status: `PASS`

Checks passed:
- Forbidden-pattern scan completed
- JSON parse succeeded
- Top-level JSON type: object; keys: clusters, compatibility, description, edge, engine, invariant, node, relation_types, schema, version
- Expected top-level keys present
- Schema identity present: AXIS-COSMOS-GRAPH-V1

### cosmos_graph

- File: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_graph.json`
- Status: `PASS`

Checks passed:
- Forbidden-pattern scan completed
- JSON parse succeeded
- Top-level JSON type: object; keys: clusters, edges, engine, generated, invariant, nodes, schema, stats
- Expected top-level keys present
- Concept nodes present: 11
- Edges reference known concept nodes: 21

### cosmos_paths

- File: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_paths.json`
- Status: `PASS`

Checks passed:
- Forbidden-pattern scan completed
- JSON parse succeeded
- Top-level JSON type: object; keys: generated, paths, schema
- Expected top-level keys present
- Named paths present: 3

### metrics_csv

- File: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Metricas.csv`
- Status: `WARN`

Checks passed:
- Forbidden-pattern scan completed
- Semicolon delimiter detected
- Expected columns present: PD#PN, PageRank, InDegree, OutDegree
- Data row count: 747
- No empty required cells found
- Metric numeric fields parse successfully

Warnings:
- CONTEXT: SQL-derived archaeology fixture; structurally valid, but not canonical until rewritten from CSL/static indexes

### edges_csv

- File: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- Status: `WARN`

Checks passed:
- Forbidden-pattern scan completed
- Semicolon delimiter detected
- Expected columns present: Source, Target
- Data row count: 7217
- No empty required cells found

Warnings:
- CONTEXT: SQL-derived archaeology fixture; structurally valid, but not canonical until rewritten from CSL/static indexes

### report_md

- File: `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/Grafo_Conexoes_Report.md`
- Status: `WARN`

Checks passed:
- Forbidden-pattern scan completed
- Markdown is non-empty UTF-8 text

Warnings:
- CONTEXT: copied archaeology Markdown is readable, but its own body lacks an explicit derived/non-canonical label

### provenance_md

- File: `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`
- Status: `WARN`

Checks passed:
- Forbidden-pattern scan completed
- Markdown is non-empty UTF-8 text
- Derived/non-canonical status is mentioned
- Provenance marker present: source path
- Provenance marker present: destination path
- Provenance marker present: Source SHA-256
- Provenance marker present: Copied SHA-256
- Provenance marker present: Review note
- Provenance marker present: Required label
- Provenance references copied file: cosmos/schemas/graph_schema.json
- Provenance references copied file: fixtures/zibaldone/cosmos_graph.json
- Provenance references copied file: fixtures/zibaldone/cosmos_paths.json
- Provenance references copied file: fixtures/zibaldone/Grafo_Metricas.csv
- Provenance references copied file: fixtures/zibaldone/Grafo_Conexoes_PDPN.csv
- Provenance references copied file: docs/rescue-20260520/Grafo_Conexoes_Report.md

Warnings:
- CONTEXT: local path pattern appears only in documentation/provenance context: /home/sanghop/
- CONTEXT: provenance marker not found via normalized matching, review formatting before relying on automation: COPY_BATCH_001 Report
- CONTEXT: provenance may not reference this file explicitly; confirm whether this is self-reference or formatting drift: fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md

## Recommended Next Action

Review non-blocking provenance/context warnings, then proceed only with explicit operator acceptance.

## Do Not Touch Confirmation

- Production touched: no.
- Published touched: no.
- Fixtures modified: no.
- More Zibaldone files copied: no.
- Git initialized: no.
- Builds, pipelines, scripts, provider/API/LLM calls: no.
- Commits, pushes, deploys: no.
