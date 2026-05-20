# COPY_BATCH_001 Report

## Operator Approval

The operator explicitly approved COPY_BATCH_001 for these reviewed AXIS-Cosmos seed materials only:

- `Grafo_Conexoes_Report.md`
- `graph_schema.json`
- `cosmos_graph.json`
- `cosmos_paths.json`
- `Grafo_Metricas.csv`
- `Grafo_Conexoes_PDPN.csv`

## Files Copied

- `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/Grafo_Conexoes_Report.md`
- `/home/sanghop/axis/axis-cosmos-lab/cosmos/schemas/graph_schema.json`
- `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_graph.json`
- `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/cosmos_paths.json`
- `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Metricas.csv`
- `/home/sanghop/axis/axis-cosmos-lab/fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`

## Files Deliberately Not Copied

- `Grafo_Constelacoes.json`
- `index.html`
- `learning_paths.json`
- `study_paths.json`
- raw SQL
- WordPress backups
- credentials
- old scripts
- generated static-site trees
- provider/API/LLM artifacts

## Safety Scan Summary

Before copying, each approved source was scanned for:

- `tenweb_backup_db.sql`
- `wp-config.php`
- `DB_PASSWORD`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `DEEPL`
- `API_KEY`
- `SECRET`
- `TOKEN`
- `/home/sanghop/`
- `/media/sanghop/`
- `.git/`
- `.venv`
- `.netlify`
- `node_modules`
- `__pycache__`
- `._`

No forbidden patterns were found in the copied candidates.

## Hash Verification Summary

All copied SHA-256 hashes match their source SHA-256 hashes. Full hash provenance is recorded in `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`.

## Validation Summary

- JSON validation passed for `graph_schema.json`, `cosmos_graph.json`, and `cosmos_paths.json`.
- CSV readability and row-shape checks passed for `Grafo_Metricas.csv` and `Grafo_Conexoes_PDPN.csv`.
- Markdown readability check passed for `Grafo_Conexoes_Report.md`.

## Do Not Touch Confirmation

- Production modified: no.
- Published modified: no.
- Git initialized: no.
- Builds run: no.
- Pipelines run: no.
- Scripts executed: no.
- Provider/API/LLM calls run: no.
- Packages installed: no.
- Repos cloned/fetched: no.
- Commits/pushes/deploys: no.
