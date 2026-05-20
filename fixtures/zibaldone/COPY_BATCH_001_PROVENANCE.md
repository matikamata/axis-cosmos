# COPY_BATCH_001 Provenance

All copied fixtures in this batch are derived, non-canonical, and local-only. AXIS-NIDDHI Canon/CSL remains the source of truth.

No raw SQL, WordPress backups, credentials, generated static-site trees, old scripts, provider/API/LLM artifacts, `Grafo_Constelacoes.json`, `index.html`, `learning_paths.json`, or `study_paths.json` were copied.

## Copied Files

| File | Source path | Destination path | Byte size | Source SHA-256 | Copied SHA-256 | Review note | Required label |
|---|---|---|---:|---|---|---|---|
| `Grafo_Conexoes_Report.md` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_Report.md` | `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/Grafo_Conexoes_Report.md` | 3277 | `7d22b09f31df79f41c77485f4fc2a4c8de979815d7a52acfff344592c6adba3d` | `7d22b09f31df79f41c77485f4fc2a4c8de979815d7a52acfff344592c6adba3d` | `docs/rescue-20260520/fixture-reviews/Grafo_Conexoes_Report_REVIEW.md` | This file is a derived Zibaldone archaeology report. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path. It is preserved only as historical Cosmos evidence. |
| `graph_schema.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/graph_schema.json` | `/home/sanghop/axis/axis-cosmos-lab/cosmos/schemas/graph_schema.json` | 2706 | `c11c2c1547147f576d56e76829fade09110be634aebf204e962f7591b7e22a1d` | `c11c2c1547147f576d56e76829fade09110be634aebf204e962f7591b7e22a1d` | `docs/rescue-20260520/fixture-reviews/graph_schema_REVIEW.md` | This schema is a derived Zibaldone/Skunkworks archaeology artifact and early AXIS-Cosmos/Navigator graph contract candidate. It is not Canon and remains experimental until accepted by the Cosmos schema process. |
| `cosmos_graph.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_graph.json` | `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_graph.json` | 7267 | `5eb063c5e707d84ff60f0430f70097096d5f5f6f3a1efe97a4b4948ecc5f6590` | `5eb063c5e707d84ff60f0430f70097096d5f5f6f3a1efe97a4b4948ecc5f6590` | `docs/rescue-20260520/fixture-reviews/cosmos_graph_REVIEW.md` | This file is a derived Zibaldone/Skunkworks concept graph fixture. It is not AXIS-NIDDHI Canon and is preserved only as an experimental Cosmos/Navigator compatibility sample. |
| `cosmos_paths.json` | `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_paths.json` | `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_paths.json` | 2503 | `44fcd0e79a9557a4c9b21044f5dfbe7607b70cc17229d172d240d609ddde75a3` | `44fcd0e79a9557a4c9b21044f5dfbe7607b70cc17229d172d240d609ddde75a3` | `docs/rescue-20260520/fixture-reviews/cosmos_paths_REVIEW.md` | This file is a derived Zibaldone/Skunkworks path fixture. It is not AXIS-NIDDHI Canon and is preserved only as an experimental Cosmos/Navigator compatibility sample. |
| `Grafo_Metricas.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Metricas.csv` | `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Metricas.csv` | 28115 | `044e9a3c8bb85844f9bff92de499da0083b6198824ac7108e1cbe6c6593a9759` | `044e9a3c8bb85844f9bff92de499da0083b6198824ac7108e1cbe6c6593a9759` | `docs/rescue-20260520/fixture-reviews/Grafo_Metricas_REVIEW.md` | This CSV is a derived Zibaldone graph-metrics artifact. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path. |
| `Grafo_Conexoes_PDPN.csv` | `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_PDPN.csv` | `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Conexoes_PDPN.csv` | 151527 | `4694996601e653d7b9576bd5e19614ca0e087a2f8acc4d4336c49c4888453a04` | `4694996601e653d7b9576bd5e19614ca0e087a2f8acc4d4336c49c4888453a04` | `docs/rescue-20260520/fixture-reviews/Grafo_Conexoes_PDPN_REVIEW.md` | This CSV is a derived Zibaldone PD#PN edge-list artifact. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path. |

## Verification

- All copied hashes match source hashes.
- JSON files validated: `graph_schema.json`, `cosmos_graph.json`, `cosmos_paths.json`.
- CSV row consistency validated: `Grafo_Metricas.csv` has 4-field rows; `Grafo_Conexoes_PDPN.csv` has 2-field rows.
- Markdown report is readable UTF-8 text.
