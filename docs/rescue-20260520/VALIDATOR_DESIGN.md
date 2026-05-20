# AXIS-Cosmos Validator Design

## 1. Purpose

Design the first future read-only validator for COPY_BATCH_001 fixtures.

This document translates `VALIDATION_SPEC.md` into a practical design for the first validator script, but it does not create code.

## 2. Design Status

- Docs-only.
- No code created.
- No scripts created.
- No execution.
- Future implementation only.

## 3. Proposed Future Script

Future script name:

`scripts/validate_fixtures_readonly.py`

Do not create it yet.

## 4. Validator Principles

Future validator must:

- be read-only by default;
- require explicit input paths;
- never touch production/published;
- never require raw SQL;
- never execute old scripts;
- never mutate fixtures;
- emit clear `PASS` / `WARN` / `FAIL` / `BLOCKED` results.

## 5. Input Set

Default future inputs:

- `cosmos/schemas/graph_schema.json`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`
- `docs/rescue-20260520/Grafo_Conexoes_Report.md`

All paths should resolve under the explicitly supplied lab root.

## 6. Validation Modules

Future internal validator components only:

- Path safety validator
  - Confirms every input path stays inside the lab and never points into production/published.
- Forbidden-pattern scanner
  - Scans candidate content for raw SQL names, credential-like strings, local private paths, cache paths, and provider/API markers.
- JSON validator
  - Parses JSON and checks expected top-level keys and rough object shapes.
- CSV validator
  - Detects delimiter, checks headers, counts rows, and flags empty required cells.
- Markdown validator
  - Confirms UTF-8 readability, archaeology status, and derived-artifact labeling.
- Provenance validator
  - Confirms each copied file is listed with source path, destination path, hashes, review note, and required label.
- Graph consistency validator
  - Performs cautious consistency checks without merging concept and PD#PN graph worlds prematurely.
- Summary reporter
  - Emits per-file results and aggregate `PASS` / `WARN` / `FAIL` / `BLOCKED` counts.

## 7. JSON Validation Design

For each JSON file:

- parse JSON;
- check expected top-level keys;
- validate rough node, edge, and path shapes;
- verify no forbidden strings;
- report schema mismatch as `WARN` or `FAIL` depending severity.

Expected checks:

- `graph_schema.json`
  - Has `schema`, `version`, `node`, `edge`, `relation_types`, and `clusters`.
- `cosmos_graph.json`
  - Has `schema`, `nodes`, `edges`, `clusters`, and `stats`.
  - Nodes should have concept-like IDs.
  - Edges should have non-empty source/target references.
- `cosmos_paths.json`
  - Has `schema`, `generated`, and `paths`.
  - Paths should contain named path records.

## 8. CSV Validation Design

For each CSV:

- detect delimiter;
- check expected columns;
- count rows;
- check empty cells;
- check PD#PN-like values where relevant;
- warn that SQL-derived fixtures remain archaeology.

Expected checks:

- `Grafo_Metricas.csv`
  - Delimiter: semicolon.
  - Columns: `PD#PN`, `PageRank`, `InDegree`, `OutDegree`.
  - `PD#PN` should look like a PD#PN identifier where possible.
  - Numeric fields should parse as numeric where possible.
- `Grafo_Conexoes_PDPN.csv`
  - Delimiter: semicolon.
  - Columns: `Source`, `Target`.
  - `Source` and `Target` must be non-empty.
  - Source/target values should look like PD#PN identifiers where possible.

## 9. Provenance Validation Design

Check:

- copied file listed in provenance;
- source path recorded;
- destination path recorded;
- source hash recorded;
- copied hash recorded;
- review note exists;
- required label exists.

Hash re-computation should be optional in the first script version but recommended when cheap.

## 10. Graph Consistency Design

Future checks:

- concept graph edges reference known concept nodes;
- path fixture references known concepts where possible;
- PD#PN edge list has `Source` and `Target`;
- metrics IDs can later be matched to known PD#PNs;
- do not merge concept graph and PD#PN graph prematurely.

Initial graph consistency should be conservative. The validator should warn about mismatches before treating them as hard failures unless the fixture is structurally unreadable.

## 11. Output Report Design

Future validator should print and optionally write a report with:

- validator version;
- timestamp or deterministic run ID;
- input files;
- check summary;
- `PASS` / `WARN` / `FAIL` / `BLOCKED` counts;
- per-file results;
- recommended next action.

The report should be concise enough for operator review but detailed enough to trace each warning or failure.

## 12. CLI Contract

Future command shape proposal:

`python3 scripts/validate_fixtures_readonly.py --root /home/sanghop/axis/axis-cosmos-lab --report outputs/validation/latest.md`

Rules:

- script should not create output unless `--report` is explicit;
- default mode may print only;
- no network;
- no provider calls.

The future script must refuse paths outside the supplied root unless an explicit design update allows external read-only references.

## 13. First Implementation Batch Proposal

Future first code batch:

- create `scripts/`;
- create `scripts/README.md`;
- create `scripts/validate_fixtures_readonly.py`;
- run it once read-only against copied fixtures;
- write report only if explicit.

Do not do this now.

## 14. Stop Conditions

Future validator must stop or `BLOCK` if:

- path points into production/published;
- raw SQL detected;
- credential-like string detected;
- local private path appears in fixture content unexpectedly;
- JSON parse fails;
- required copied fixture missing.

`BLOCKED` means the operator should review before any further validation or copy/migration work continues.

## 15. Next Safe Step

Create the first read-only validator script in one controlled batch, with no git, no deploy, no provider calls.

## 16. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/VALIDATOR_DESIGN.md`; updated `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COSMOS_OPERATOR_DASHBOARD.md`.
- Production touched: no.
- Published touched: no.
- More Zibaldone files copied: no.
- Code or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
