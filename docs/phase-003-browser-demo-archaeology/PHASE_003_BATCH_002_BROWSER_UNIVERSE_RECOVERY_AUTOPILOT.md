# PHASE 003 Batch 002 Browser Universe Recovery Autopilot

## Purpose

Recover a richer local browser Cosmos universe view from already copied AXIS-Cosmos fixtures, without using old scripts, external dependencies, or protected environments.

## Old UI Archaeology Findings

- Legacy browser page used D3 and a full constellation JSON reference.
- Legacy page depended on external CDN loading.
- Legacy page expected server-style JSON loading behavior.
- This was not safe to reuse directly under current local-only, no-network constraints.

## Direct Copy Decision

Old UI was not copied directly.

## Data Generation Method

- Parsed PD#PN edges from `Grafo_Conexoes_PDPN.csv`.
- Parsed PD#PN metrics from `Grafo_Metricas.csv`.
- Built node/edge universe in a generated local JS data bundle.
- Enriched PD#PN nodes with PageRank/InDegree/OutDegree where available.
- Added concept/path context subset from `cosmos_graph.json` and `cosmos_paths.json`.
- Stored derived dataset as `browser-demo/data/axis_cosmos_universe.js` for file-open compatibility.

## Source Fixtures Used

- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`

## Files Created or Modified

Created:
- `browser-demo/data/axis_cosmos_universe.js`
- `docs/phase-003-browser-demo-archaeology/PHASE_003_BATCH_002_BROWSER_UNIVERSE_RECOVERY_AUTOPILOT.md`

Modified:
- `browser-demo/index.html`
- `browser-demo/demo.js`
- `browser-demo/style.css`
- `browser-demo/README.md`

## Graph Counts

- Full PD#PN nodes: 747
- Full PD#PN edges: 7217
- Rendered PD#PN nodes in default universe view: 260
- Rendered PD#PN edges in default universe view: 2104
- Metric rows: 747
- Concept sample source nodes: 11
- Concept sample source edges: 21
- Concept paths: 3

## How To Open

Open `browser-demo/index.html` directly in a browser (`file://`).

## Known Limitations

- Rendering uses a subset for smooth local drawing; full counts are still shown.
- Layout is deterministic and lightweight, not physics-based.
- Concept view is a context sample, not a full recovery of legacy constellation behavior.
- Demo remains derived/non-canonical archaeology context only.

## Safety Scan Result

- No credential-like patterns found.
- No SQL/backup indicators found.
- No external network dependencies in created/modified browser demo files.
- No production/published references leaked into browser-visible content.

## Do Not Touch Confirmation

- Production touched: no.
- Published touched: no.
- Fixtures modified: no.
- Copied seed files modified: no.
- Old Zibaldone scripts executed: no.
- Builds/pipelines/provider/API/LLM/network calls: no.
