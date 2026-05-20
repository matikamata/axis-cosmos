# AXIS-Cosmos Browser Demo

Local-only Cosmos universe archaeology demo.

Derived and non-canonical: this is not Canon and not a source-of-truth replacement for CSL, identity records, lineage records, or future validated graph outputs.

## How To Open

Open `browser-demo/index.html` directly in your browser (`file://` flow, no server required).

## Data Sources

- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`

## What It Shows

- Dynamic force-style PD#PN universe with node repulsion, spring edges, center gravity, and damping.
- Stabilized physics lifecycle with alpha cooling, auto-settle, velocity/displacement caps, and close-range force clamps.
- Draggable nodes, hover neighborhood highlight, click-to-lock detail panel, zoom/pan, and search-centering.
- Render controls: Top 100 / Top 260 / Top 500 / Full graph experimental.
- Controls: Pause/Resume, Reset Layout, Settle Now, Reheat, and Auto-settle toggle.
- Full-window-first layout with compact sticky controls and a toggleable side panel.
- DPR-aware pointer mapping plus nearest-node hit testing with forgiving click radius.
- Clear Selection and Focus Universe controls for faster operator flow.
- Concept graph sample view with path snippets.
- Full-count summary for the copied fixture universe.

## Safety and Scope

- Vanilla HTML/CSS/JS only (no CDN, no external libraries).
- Local-only usage; no deploy target.
- No fixture mutation and no production/published interaction.
