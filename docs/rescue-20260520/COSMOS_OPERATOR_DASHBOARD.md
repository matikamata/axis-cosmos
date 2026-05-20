# AXIS-Cosmos Operator Dashboard

## 1. Current State

`axis-cosmos-lab` is local-only and docs-first. COPY_BATCH_001 is completed for the first reviewed safe seed materials.

Local scripts exist (`validate_fixtures_readonly.py`, `analyze_fixtures_readonly.py`) and are scoped to read-only fixture inspection and reporting.

No builds, pipelines, provider/API/LLM calls, git initialization, commits, pushes, or deploys have happened in this rescue lane.

## 2. Reviewed Candidates

Completed reviews: 10.

- `Grafo_Conexoes_Report.md`
- `graph_schema.json`
- `cosmos_graph.json`
- `cosmos_paths.json`
- `Grafo_Metricas.csv`
- `Grafo_Conexoes_PDPN.csv`
- `Grafo_Constelacoes.json`
- `index.html`
- `learning_paths.json`
- `study_paths.json`

## 3. Copied In COPY_BATCH_001

- `docs/rescue-20260520/Grafo_Conexoes_Report.md`
- `cosmos/schemas/graph_schema.json`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`

All copied files are derived, non-canonical, local-only seed materials. Provenance is recorded in `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`.

## 4. Pending / Boundary Candidates

- `Grafo_Constelacoes.json`: sample-only later; do not copy whole.
- `index.html`: UI archaeology docs-only; do not copy as runnable UI.
- `learning_paths.json`: pending Navigator/Academy boundary.
- `study_paths.json`: pending Navigator/Academy boundary.

## 5. Blocked / Do Not Copy Candidates

No candidate is blocked by credential/raw-SQL scan results in this batch.

Still do not copy: raw SQL, WordPress backups, credentials, generated static-site trees, `.git`, `.venv`, `.netlify`, `node_modules`, cache files, AppleDouble files, provider/API/LLM artifacts, or old executable scripts.

## 6. Next Recommended Action

Create a docs-only COPY_BATCH_001 integration plan before writing any code. The plan should decide whether `graph_schema.json` is accepted as-is, forked from Navigator, or revised into a Cosmos-native `GraphBundle` schema.

Status: `COPY_BATCH_001_INTEGRATION_PLAN.md` now exists. Next recommended action is `VALIDATION_SPEC.md`.

Status: `VALIDATION_SPEC.md` now exists. Next recommended action is docs-only `VALIDATOR_DESIGN.md`.

Status: `VALIDATOR_DESIGN.md` now exists. Next recommended action is one controlled read-only validator script batch.

Status: first read-only validator exists and was rerun with tightened non-blocking WARN wording. Report: `outputs/validation/COPY_BATCH_001_VALIDATION_REPORT.md` (`PASS=4`, `WARN=4`, `FAIL=0`, `BLOCKED=0`).

Status: `DERIVED_ARTIFACT_LABELS.md` now documents `Grafo_Conexoes_Report.md` as a derived, non-canonical archaeology/context artifact without editing the copied report.

## 7. Batch 007 Cross-References

- Analysis report: `outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md` (derived/non-canonical context output).
- Fixture inventory: `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md` (index only; not a graph).
- Artifact labeling note: `docs/rescue-20260520/DERIVED_ARTIFACT_LABELS.md`.

`docs/rescue-20260520/Grafo_Conexoes_Report.md` remains a derived archaeology/context artifact and not authoritative graph truth.

CSL, identity records, lineage records, and future validated graph outputs remain authoritative.

## 8. Derived Label Nuance

`docs/rescue-20260520/Grafo_Conexoes_Report.md` may not embed a derived/non-canonical label in its own body.

Its boundary status is maintained by `DERIVED_ARTIFACT_LABELS.md`, fixture review notes, `COPY_BATCH_001_PROVENANCE.md`, and validation/analysis report context.

Do not edit `Grafo_Conexoes_Report.md` to force in-file labeling during this rescue docs lane.

Approval checkpoint: `COSMOS_BATCH_010B_APPROVAL_CHECKPOINT.md` accepts 010b and authorizes only a narrow, read-only Batch 011 scope.
