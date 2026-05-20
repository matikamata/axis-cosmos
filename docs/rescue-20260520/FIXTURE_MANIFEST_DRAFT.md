# Fixture Manifest Draft

## 1. Purpose

This is a planning manifest for future AXIS-Cosmos fixture migration. It lists candidate files, expected classes, and planned destinations only.

No Zibaldone seed material is copied by this document.

## 2. Manifest Status

- Draft only.
- No fixtures copied.
- No schemas created.
- No code created.
- All candidates require sanitization review first.
- Derived fixtures are not Canon.

AXIS-Cosmos fixtures, when accepted later, must be treated as derived graph artifacts with clear provenance. AXIS-NIDDHI Canon/CSL remains the source of truth.

## 3. Planned Future Directories

Proposed future directories only, not created in this pass:

- `fixtures/zibaldone/`
- `cosmos/schemas/`
- `docs/rescue-20260520/`
- `docs/rescue-20260520/fixture-reviews/`

## 4. Candidate Fixture Table

| Candidate | Source path | Class | Planned destination | Review status | Copy decision | Notes |
|---|---|---|---|---|---|---|
| `Grafo_Conexoes_Report.md` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_Report.md` | `DOC_SAFE_CANDIDATE` | `docs/rescue-20260520/` or `docs/rescue-20260520/fixture-reviews/` | pending | not yet | Needs provenance note, local path review, and generated-report labeling before copy. |
| `Grafo_Metricas.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Metricas.csv` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/Grafo_Metricas.csv` | pending | not yet | Needs size check, column review, SQL-derived provenance, and public-safety scan. |
| `Grafo_Conexoes_PDPN.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_PDPN.csv` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv` | pending | not yet | Needs size check, PD#PN relation review, unknown slug review, and SQL-derived provenance. |
| `Grafo_Constelacoes.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Constelacoes.json` | `LARGE_FIXTURE_SAMPLE_ONLY` | `fixtures/zibaldone/sample_Grafo_Constelacoes.json` | pending | not yet | Must not be copied whole initially; needs size review, forbidden-string scan, and sampling method. |
| `index.html` | `/home/sanghop/axis/Zibaldone_20260519_22h22/index.html` | `UI_ARCHAEOLOGY_DOC_ONLY` | `docs/rescue-20260520/fixture-reviews/` or future UI archaeology note | pending | not yet | Needs external dependency review, embedded data review, and should be documented before any runnable UI exists. |
| `graph_schema.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/graph_schema.json` | `SCHEMA_SAFE_CANDIDATE` | `cosmos/schemas/graph_schema.json` | pending | not yet | Needs schema acceptance, Navigator compatibility review, and provenance fields decision. |
| `cosmos_graph.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_graph.json` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/cosmos_graph.json` | pending | not yet | Needs size check, schema-shape review, stale assumption review, and forbidden-string scan. |
| `cosmos_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_paths.json` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/cosmos_paths.json` | pending | not yet | Needs Navigator path compatibility review, provenance note, and boundary decision. |
| `learning_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/learning_paths.json` | `CROSS_REPO_REDIRECT` | `fixtures/zibaldone/learning_paths.json` or Navigator/Academy notes | pending | not yet | Needs ownership decision across Cosmos, Navigator, and Academy before copy. |
| `study_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/study_paths.json` | `CROSS_REPO_REDIRECT` | `fixtures/zibaldone/study_paths.json` or Navigator/Academy notes | pending | not yet | Needs study-path schema boundary review and ownership decision before copy. |

## 5. Candidate Destination Notes

Docs and report materials should go to `docs/rescue-20260520/` or fixture review notes. They should preserve archaeology context without pretending to be active schema or fixture content.

Schemas should move only after schema acceptance. The first schema candidate should be compared against the current Navigator graph schema and the Cosmos schema notes before it enters `cosmos/schemas/`.

Small fixtures should move only after string, path, credential-like, and size scans. They must also carry provenance and derived-artifact labels.

Large JSON should enter only as a trimmed sample. The original file size and later sampling method should be recorded.

UI archaeology should become documentation first, not runnable UI. Any future renderer should be rewritten intentionally against accepted Cosmos schema contracts.

## 6. Review Workflow

1. Classify candidate.
2. Run checklist.
3. Record provenance.
4. Decide destination.
5. Create review note.
6. Only then copy in a future pass.

## 7. Not Copy-Ready Yet

None of these candidates are copy-ready yet because:

- no file-size review has been completed;
- no forbidden string scan has been completed;
- no credential-like scan has been completed;
- no provenance note exists per file;
- no fixture destination folder exists;
- no operator approval has been recorded.

## 8. First Likely Safe Copy Candidates Later

1. `Grafo_Conexoes_Report.md`
2. `graph_schema.json`
3. `cosmos_graph.json`
4. `cosmos_paths.json`
5. `Grafo_Metricas.csv`

These are likely safer than the large D3 JSON or old HTML because they are either documentation, schema-like material, or smaller fixture candidates. They still require the full sanitization checklist before any copy.

## 9. Deferred / Sample-Only Candidates

- `Grafo_Constelacoes.json`: sample-only later; do not copy whole initially.
- `index.html`: UI archaeology docs first; do not copy as runnable UI yet.
- `learning_paths.json`: pending Navigator/Academy boundary review.
- `study_paths.json`: pending Navigator/Academy boundary review.

## 10. Next Safe Step

Create `fixtures/` and `docs/rescue-20260520/fixture-reviews/` only after this manifest is accepted, still without copying Zibaldone files.

## 11. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/FIXTURE_MANIFEST_DRAFT.md`.
- Production touched: no.
- Published touched: no.
- Zibaldone files copied: no.
- Schemas, fixtures, code folders, or scripts created: no.
- Git initialized: no.
- Clone/fetch/commit/push/deploy happened: no.
- Builds, pipelines, scripts, or provider calls ran: no.
