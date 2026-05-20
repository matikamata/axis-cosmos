# COSMOS Analyzer Skeleton Design

## 1. Purpose

This document designs a future AXIS-Cosmos analyzer skeleton for inspecting copied COPY_BATCH_001 fixtures and derived archaeology artifacts.

The future analyzer should help operators understand graph shape, fixture consistency, metric summaries, and possible relationships between concept/path fixtures and PD#PN post-link fixtures.

It must not treat copied artifacts as canonical truth.

## 2. Non-Goals

The future analyzer must not:

- mutate Canon or CSL;
- replace AXIS-NIDDHI;
- certify any graph as authoritative;
- execute old Zibaldone scripts;
- read raw SQL or WordPress backups;
- call providers/API/LLM services;
- run builds or pipelines;
- deploy anything;
- write outputs unless an explicit output path is provided.

## 3. Input Boundaries

Allowed future inputs:

- `cosmos/schemas/graph_schema.json`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- `docs/rescue-20260520/Grafo_Conexoes_Report.md`
- `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`
- read-only validation reports under `outputs/validation/`

Forbidden inputs:

- raw SQL;
- WordPress backups;
- credentials;
- provider/API/LLM artifacts;
- old executable Zibaldone scripts;
- production/published files;
- generated static-site trees.

CSL, identity records, lineage records, and future validated graph outputs remain the authority.

## 4. Output Boundaries

Future analyzer outputs should be explicit, derived, local-only reports.

Allowed future output area:

- `outputs/analysis/`

Output files should be Markdown or JSON summaries only after explicit operator approval.

The analyzer must not overwrite fixtures, schemas, rescue docs, production, published, or Canon sources.

## 5. Read-Only Safety Rules

The future analyzer must:

- require an explicit `--root`;
- refuse roots inside production/published;
- resolve every input path before reading;
- refuse paths outside the lab unless explicitly approved in a later design;
- never modify fixtures;
- never call network;
- never import old project scripts;
- never execute shell commands;
- never write unless an explicit `--report` path is provided;
- mark all findings as derived observations.

## 6. Proposed Module Shape

Future implementation shape:

- `cosmos_analyzer.path_safety`
  - Validates root, inputs, and output path boundaries.
- `cosmos_analyzer.loaders`
  - Loads JSON, CSV, and Markdown artifacts with standard-library parsers.
- `cosmos_analyzer.concept_graph`
  - Summarizes concept nodes, edges, clusters, and paths from `cosmos_graph.json` and `cosmos_paths.json`.
- `cosmos_analyzer.pdpn_graph`
  - Summarizes PD#PN edge list size, metric coverage, top degree candidates, and orphan-like hints.
- `cosmos_analyzer.bridge`
  - Reports possible conceptual bridges between the two graph worlds without forcing a merge.
- `cosmos_analyzer.provenance`
  - Carries forward COPY_BATCH_001 provenance labels and non-canonical warnings.
- `cosmos_analyzer.reporter`
  - Emits an operator-readable derived analysis report.

No module files are created in this batch.

## 7. Proposed CLI Contract

Future command shape:

`python3 scripts/analyze_fixtures_readonly.py --root /home/sanghop/axis/axis-cosmos-lab --report outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md`

Rules:

- `--root` required;
- `--report` optional;
- no report written unless `--report` is provided;
- report path must be under `outputs/analysis/`;
- no network;
- no provider calls;
- no mutation of fixtures or docs.

## 8. Proposed Report Format

Future report sections:

- analyzer name/version;
- run timestamp or deterministic run ID;
- root path;
- input files inspected;
- concept graph summary;
- path summary;
- PD#PN edge-list summary;
- metrics summary;
- possible bridge observations;
- provenance summary;
- warnings and caveats;
- recommended next action;
- do-not-touch confirmation.

Reports should distinguish facts observed in copied fixtures from interpretation.

## 9. Provenance Labeling Rules

Every future analyzer output must state:

- inputs are copied rescue fixtures/artifacts;
- outputs are derived and non-canonical;
- SQL-derived artifacts remain archaeology until rewritten from CSL/static indexes;
- Navigator-compatible artifacts are compatibility samples, not ownership decisions;
- CSL, identity records, lineage records, and future validated graph outputs remain authoritative.

Suggested report label:

“This analysis is derived from COPY_BATCH_001 rescue fixtures. It is not Canon, not an authoritative AXIS-Cosmos graph, and not a replacement for CSL, identity records, lineage records, or future validated graph outputs.”

## 10. Stop Conditions

The future analyzer must stop or refuse to run if:

- root points into production/published;
- any input path points into production/published;
- raw SQL is requested;
- credentials or provider artifacts are detected;
- required copied fixtures are missing;
- JSON/CSV parsing fails before analysis;
- output path is outside the approved analysis output area;
- an old Zibaldone script would be needed.

## 11. Derived / Non-Canonical Statement

Future analyzer outputs are derived and non-canonical until validated.

They may inspect copied fixtures and derived archaeology artifacts, but they must not treat them as canonical truth. CSL, identity records, lineage records, and future validated graph outputs remain the authority.

## 12. Do Not Touch Confirmation

- File created: `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COSMOS_ANALYZER_SKELETON_DESIGN.md`.
- Scripts/code created: no.
- `scripts/validate_fixtures_readonly.py` edited: no.
- Copied artifacts or fixtures modified: no.
- `Grafo_Conexoes_Report.md` edited: no.
- Production touched: no.
- Published touched: no.
- Git initialized: no.
- Builds, pipelines, extractors, analyzers, or provider calls run: no.
