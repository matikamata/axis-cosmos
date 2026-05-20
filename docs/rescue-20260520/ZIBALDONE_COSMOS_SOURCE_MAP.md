# Zibaldone Cosmos Source Map

## 1. Purpose

This is a docs-only source map for future sanitized migration into AXIS-Cosmos. It identifies the first Cosmos seed materials in Zibaldone and records why they matter, where they currently live, what risks they carry, and where they may belong later.

No Zibaldone files are copied by this map. Sanitization, size review, and source-boundary review come later.

## 2. Source Roots

- `/home/sanghop/axis/Zibaldone_20260519_22h22`
- `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados`
- `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga`

## 3. Primary Cosmos Seeds

| Seed | Source path | Type | Why it matters | Risk | Future destination | Copy now? |
|---|---|---|---|---|---|---|
| `Grafo_Conexoes_Report.md` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_Report.md` | report / doc seed | Captures graph extraction summary, node/edge counts, top source/target posts, and unknown slugs. | Low; generated report still needs provenance note. | `docs/rescue-20260520/ZIBALDONE_COSMOS_SOURCE_MAP.md` reference or future fixture notes. | no |
| `Grafo_Metricas.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Metricas.csv` | graph metric fixture | Contains PageRank, in-degree, and out-degree output from the Zibaldone analyzer. | Low-medium; generated data should be checked against canonical source. | `fixtures/zibaldone/Grafo_Metricas.csv` after sanitization. | no |
| `Grafo_Conexoes_PDPN.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_PDPN.csv` | edge-list fixture | Contains PD#PN source-target relationships useful for Cosmos graph prototypes. | Medium; derived from SQL-dependent extraction, so provenance must be explicit. | `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv` after sanitization. | no |
| `Grafo_Constelacoes.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Constelacoes.json` | D3 graph fixture | Large node/link artifact for constellation visualization. | Medium-high; size review and trim/sample decision required. | `fixtures/zibaldone/sample_Grafo_Constelacoes.json` after trimming. | no |
| `index.html` | `/home/sanghop/axis/Zibaldone_20260519_22h22/index.html` | UI archaeology | D3 constellation prototype with section filtering and PageRank-scaled nodes. | Medium; external D3 CDN and prototype assumptions need review. | `docs/rescue-20260520/COSMOS_UI_ARCHAEOLOGY.md` or future renderer notes. | no |
| `graph_schema.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/graph_schema.json` | schema seed | Defines the early AXIS-COSMOS graph schema and compatibility intent. | Low; already matched current Navigator graph schema in prior inventory. | `cosmos/schemas/graph_schema.json` after schema acceptance. | no |
| `cosmos_graph.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_graph.json` | graph fixture | Small concept graph example for schema and renderer tests. | Low; verify no stale semantic assumptions. | `fixtures/zibaldone/cosmos_graph.json`. | no |
| `cosmos_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_paths.json` | path fixture | Example path output for concept/study route rendering. | Low; compare with Navigator path contract. | `fixtures/zibaldone/cosmos_paths.json`. | no |
| `learning_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/learning_paths.json` | learning-path fixture | Supports study-order and Academy/Cosmos route ideas. | Low; belongs partly to Navigator/Academy, so destination should be cross-referenced. | `fixtures/zibaldone/learning_paths.json` or cross-repo doc. | no |
| `study_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/study_paths.json` | study-path fixture | Defines sequential study path examples useful for graph route overlays. | Low; belongs partly to Navigator/Academy, so destination should be cross-referenced. | `fixtures/zibaldone/study_paths.json` or cross-repo doc. | no |

Reason for all `Copy now? no`: this pass is mapping only. Sanitization comes later.

## 4. Script Archaeology

| Script | Old role | Why useful | Why not safe to execute/copy directly | Rewrite direction |
|---|---|---|---|---|
| `ligue_os_pontos.py` | Extract PD#PN links from raw WordPress SQL plus MasterPDPN metadata. | Preserves the first practical link-extraction model for Cosmos. | SQL-dependent; may touch raw source assumptions; writes generated graph outputs. | Rewrite against current CSL-derived metadata and sanitized static indexes. |
| `analisar_grafo.py` | Load edge CSV and calculate PageRank, in-degree, and out-degree via NetworkX. | Captures useful graph metrics for hub discovery. | Writes metrics output and depends on local generated CSV state. | Rewrite as pure analyzer functions with explicit input/output paths and tests. |
| `gerar_json_d3.py` | Convert raw metadata, edge CSV, and metrics CSV into D3 node/link JSON. | Shows how Cosmos constellation fixtures were assembled. | Implicit local paths and writes large JSON output. | Rewrite around stable Cosmos schema and small fixture generation. |
| `cosmos_engine.py` | Build, analyze, export, and serve Cosmos graph artifacts. | Contains early engine shape for clusters, gravity, paths, and visual output. | Includes CLI/server/build side effects; should not be executed in archaeology mode. | Split into pure library functions, CLI adapter, and renderer/exporter later. |
| `graph_builder.py` | Build concept graph artifacts from concept/path data. | Useful for schema assumptions and graph construction rules. | Old prototype may duplicate Navigator and may encode stale assumptions. | Review API, extract schema notes, then rewrite or keep in Navigator boundary. |

## 5. Forbidden Material

Do not copy into Cosmos:

- raw SQL;
- WordPress backup trees;
- `wp-config.php`;
- credentials;
- `.git`;
- `.venv`;
- `.netlify`;
- `node_modules`;
- pyc/cache files;
- AppleDouble files;
- generated static-site trees;
- provider/API/LLM artifacts.

## 6. Future Sanitization Pass

Next pass should:

- inspect file sizes;
- confirm no secrets;
- trim large JSON if needed;
- copy only docs, schemas, and small fixtures;
- keep SQL-dependent code as archaeology docs;
- avoid all code execution.

The first likely copy candidates are docs and small schema/fixture files. The large D3 graph JSON should be sampled or trimmed before entering the lab.

## 7. Do Not Touch Confirmation

Files created/modified:

- Modified `/home/sanghop/axis/axis-cosmos-lab/README.md`.
- Created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/ZIBALDONE_COSMOS_SOURCE_MAP.md`.

Protected paths:

- `/home/sanghop/axis/axis-niddhi-production`: not touched.
- `/home/sanghop/axis/axis-niddhi-published`: not touched.

Execution safety:

- No Zibaldone files were copied.
- Git was not initialized.
- No builds were run.
- No pipelines were run.
- No scripts were executed.
- No provider/API/LLM calls were run.
- No commits were made.
- No pushes were made.
- No deploys were made.

