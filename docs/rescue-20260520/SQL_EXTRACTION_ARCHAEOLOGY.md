# SQL Extraction Archaeology

## 1. Purpose

This document records the historical SQL-dependent AXIS-Cosmos extraction method so it can be rewritten safely later against CSL-derived metadata or sanitized static indexes.

It does not copy SQL, WordPress backup material, Zibaldone fixtures, or old executable code. The old scripts remain archaeology only.

## 2. Historical Role

The old Cosmos extraction path appears to have used three local scripts:

- `ligue_os_pontos.py`
  - Read raw WordPress SQL and `MasterPDPN_Raw.csv`.
  - Detected published WordPress post tuples.
  - Mapped slugs to PD#PN identifiers.
  - Extracted internal links and emitted PD#PN-to-PD#PN edges.
  - Reported unknown slugs.
- `analisar_grafo.py`
  - Read the generated PD#PN edge CSV.
  - Built a directed graph with NetworkX.
  - Calculated PageRank, in-degree, and out-degree.
  - Wrote graph metrics CSV.
- `gerar_json_d3.py`
  - Read MasterPDPN metadata, edge CSV, and metrics CSV.
  - Built D3-compatible node/link JSON.
  - Added PageRank and section/group metadata for constellation rendering.

Apparent old flow:

```text
raw WordPress SQL + MasterPDPN metadata
  -> PD#PN link edge list
  -> graph metrics
  -> D3 constellation JSON
  -> prototype index.html
```

## 3. Why This Was Valuable

The historical approach captured several useful Cosmos ideas:

- extracting PD#PN-to-PD#PN relationships from internal corpus links;
- identifying graph hubs in the corpus;
- computing PageRank, in-degree, and out-degree;
- producing visual constellation data;
- exposing unknown slugs or broken/ambiguous links;
- creating raw material for future Cosmos, Navigator, and Academy study paths;
- showing how section codes can become graph groups or visual filters;
- proving that a full-corpus relationship map is feasible.

## 4. Why This Must Not Be Reused Directly

The old extraction path must not be reused directly because it has several risks:

- raw SQL dependency;
- WordPress backup dependency;
- possible credential-adjacent files nearby in backup trees;
- implicit writes to generated CSV/JSON/report outputs;
- unknown assumptions about local source paths;
- generated outputs mixed with source inputs;
- not safe for a public repo;
- not aligned with the current Canon-first architecture;
- no explicit fixture-safety checks;
- no stable Cosmos schema boundary;
- old scripts combine extraction, reporting, and file writes too tightly.

The valuable part is the model, not the old execution path.

## 5. Rewrite Direction

Future Cosmos extraction should use a safer rewrite:

- no SQL input;
- no WordPress backup input;
- read from CSL-derived metadata or sanitized static indexes;
- pure functions first;
- explicit input paths;
- explicit output paths;
- no implicit writes;
- small fixtures first;
- tests before UI;
- output a stable Cosmos schema;
- keep old scripts as archaeology only;
- keep all generated artifacts marked as derived, not canonical.

The rewritten extractor should treat AXIS-NIDDHI/Canon as read-only and should never mutate source content.

## 6. Candidate Future Modules

Possible future module ideas:

- `cosmos.extractors.pdpn_links`
  - Extract safe PD#PN relationships from CSL-derived/static metadata.
- `cosmos.analyzers.graph_metrics`
  - Calculate PageRank, degree metrics, clusters, and hub summaries from sanitized edge lists.
- `cosmos.renderers.d3_export`
  - Export small D3-compatible fixtures from stable Cosmos graph objects.
- `cosmos.schemas.graph`
  - Define stable node, edge, metric, path, and provenance structures.
- `cosmos.validators.fixture_safety`
  - Check size, forbidden paths, credential-like content, and generated/source boundaries before fixture promotion.

No module is created in this pass.

## 7. Known Historical Outputs

Known historical outputs, not copied here:

- `Grafo_Conexoes_PDPN.csv`
- `Grafo_Metricas.csv`
- `Grafo_Constelacoes.json`
- `Grafo_Conexoes_Report.md`
- `index.html`

These remain in Zibaldone until a later sanitization pass decides what can safely enter `axis-cosmos-lab`.

## 8. Forbidden Inputs

The future Cosmos lab must not ingest or store:

- `tenweb_backup_db.sql`;
- raw WordPress backup trees;
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

## 9. Next Safe Step

Next docs-only document:

- `COSMOS_SCHEMA_NOTES.md`

Do not create it in this pass.

## 10. Do Not Touch Confirmation

Files created/modified:

- Created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/SQL_EXTRACTION_ARCHAEOLOGY.md`.

Protected paths:

- `/home/sanghop/axis/axis-niddhi-production`: not touched.
- `/home/sanghop/axis/axis-niddhi-published`: not touched.

SQL and source safety:

- SQL was not copied.
- Raw SQL contents were not opened.
- Raw SQL contents were not printed.
- WordPress backups were not copied.

Execution safety:

- Zibaldone scripts were not executed.
- Zibaldone fixtures were not copied.
- Git was not initialized.
- No builds were run.
- No pipelines were run.
- No provider/API/LLM calls were run.
- No commits were made.
- No pushes were made.
- No deploys were made.

