# AXIS-Cosmos Validation Spec

## 1. Purpose

This is the docs-only validation contract for COPY_BATCH_001 before any validator code exists.

It defines what future validators should check for the copied AXIS-Cosmos seed materials, how results should be reported, and what must remain out of scope until the lab is ready for code.

## 2. Validation Scope

This spec covers:

- copied JSON fixtures;
- copied CSV fixtures;
- copied Markdown archaeology report;
- copied graph schema candidate;
- provenance file;
- future validator expectations.

Current COPY_BATCH_001 copied seed count: 6.

## 3. Non-Goals

This spec does not:

- validate Canon;
- mutate CSL;
- run extraction;
- run graph analysis;
- run D3 rendering;
- call providers/API/LLM;
- certify public release readiness.

## 4. Global Validation Rules

Future validators must:

- be read-only by default;
- use explicit input paths;
- never write unless an output path is explicit;
- never touch production/published;
- never require raw SQL or WordPress backups;
- never execute old scripts;
- report pass/fail/warn clearly.

Validators should treat all COPY_BATCH_001 files as derived, local-only, non-canonical seed material.

## 5. JSON Validation Requirements

Files:

- `cosmos/schemas/graph_schema.json`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`

Required checks:

- valid JSON;
- expected top-level keys;
- no forbidden patterns;
- no local absolute paths;
- schema identity if present;
- node/edge/path shape checks;
- provenance requirement.

Expected top-level shape:

- `graph_schema.json`: `schema`, `version`, `engine`, `node`, `edge`, `relation_types`, `clusters`, `compatibility`.
- `cosmos_graph.json`: `schema`, `generated`, `engine`, `nodes`, `edges`, `clusters`, `stats`.
- `cosmos_paths.json`: `schema`, `generated`, `paths`.

## 6. CSV Validation Requirements

Files:

- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`

Required checks:

- readable text;
- expected delimiter;
- expected columns;
- row count;
- no forbidden patterns;
- PD#PN-looking values where relevant;
- no empty source/target rows;
- SQL-derived provenance warning.

Expected columns:

- `Grafo_Metricas.csv`: `PD#PN`, `PageRank`, `InDegree`, `OutDegree`.
- `Grafo_Conexoes_PDPN.csv`: `Source`, `Target`.

## 7. Markdown Validation Requirements

Files:

- `docs/rescue-20260520/Grafo_Conexoes_Report.md`
- provenance/report docs

Required checks:

- UTF-8 readable;
- derived-artifact label present or required;
- no forbidden strings;
- no unsafe local paths;
- no credential-like content;
- archaeology status clear.

Markdown reports should remain explanatory evidence. They should not become canonical data sources.

## 8. Provenance Validation

Every accepted fixture should be traceable to:

- source path;
- copied destination;
- SHA-256 source hash;
- SHA-256 copied hash;
- review note;
- required label;
- copy batch report.

For COPY_BATCH_001, the primary provenance record is `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`.

## 9. Graph Consistency Checks

Future checks should include:

- every edge source/target resolves to a known node where applicable;
- PD#PN edge list has non-empty `Source`/`Target`;
- metrics rows map to known PD#PNs where possible;
- concept graph nodes/edges align with graph schema candidate;
- path fixture references known concept IDs where possible.

Consistency checks should report warnings before they enforce failures, because these fixtures are archaeology seeds.

## 10. Two Graph Worlds

Validation must explicitly separate:

- Navigator-style concept/path graph;
- SQL-derived PD#PN/post-link graph.

Validators should not force these into one schema prematurely. The concept/path graph can validate against the early `AXIS-COSMOS-GRAPH-V1` candidate. The PD#PN/post-link graph should validate as SQL-derived archaeology until it is rewritten from CSL/static indexes.

## 11. Severity Levels

- `PASS`
  - Example: JSON parses successfully and expected top-level keys exist.
- `WARN`
  - Example: fixture is valid but SQL-derived, experimental, or overlaps with Navigator ownership.
- `FAIL`
  - Example: JSON does not parse, CSV columns are missing, or required source/target fields are empty.
- `BLOCKED`
  - Example: credential-like content, raw SQL content, protected path targeting, or provider/API execution requirement is detected.

## 12. Future Validator Output Shape

Future validation reports should include:

- file;
- validator;
- status;
- checks passed;
- warnings;
- failures;
- provenance summary;
- recommended action.

The report should be readable by an operator before any automated decision is made.

## 13. First Validator Implementation Plan

No code now. Recommended later sequence:

1. `validate_fixtures_readonly.py`
2. JSON shape checks first
3. CSV shape checks second
4. provenance checks third
5. graph consistency checks later

The first implementation should be pure, read-only, and explicit about all input paths.

## 14. Deferred Items

- `Grafo_Constelacoes.json`: sample-only later.
- `index.html`: UI archaeology only.
- `learning_paths.json`: Navigator/Academy boundary pending.
- `study_paths.json`: Navigator/Academy boundary pending.
- Old scripts: rewrite only.
- Raw SQL, backups, credentials: forbidden.

## 15. Next Safe Step

Create a docs-only `VALIDATOR_DESIGN.md` before writing the first validator script.

## 16. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/VALIDATION_SPEC.md`; updated `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COSMOS_OPERATOR_DASHBOARD.md`.
- Production touched: no.
- Published touched: no.
- More Zibaldone files copied: no.
- Code or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
