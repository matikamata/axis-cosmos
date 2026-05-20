# PHASE_003_BATCH_003_FORCE_UNIVERSE_INTERACTION_AUTOPILOT

## Purpose

Upgrade the local-only Cosmos browser demo from static spiral-like rendering to a dynamic force-style interactive universe using only vanilla JavaScript.

## Old UI Findings

- Legacy UI used D3 force simulation behavior.
- Legacy UI supported drag interaction, zoom/pan, radius by weight, and color grouping.
- Legacy UI depended on external CDN and server-oriented loading assumptions.

## Old UI Copied Directly

No. Behavior was emulated in clean local code without direct legacy copy.

## Files Modified

- `browser-demo/index.html`
- `browser-demo/demo.js`
- `browser-demo/style.css`
- `browser-demo/README.md`
- `browser-demo/data/axis_cosmos_universe.js` (regenerated from copied fixtures only)

## Files Created

- `docs/phase-003-browser-demo-archaeology/PHASE_003_BATCH_003_FORCE_UNIVERSE_INTERACTION_AUTOPILOT.md`

## Interaction Features Implemented

- requestAnimationFrame simulation loop
- node repulsion force
- edge spring force
- center gravity force
- damping/friction stabilization
- pause/resume physics button
- reset layout button
- draggable nodes with release back to simulation
- hover highlight for node and connected neighborhood
- click-to-lock node details
- search by PD#PN or concept id with camera recentering
- zoom and pan controls

## Visual Encodings Implemented

- node size by PageRank/gravity with degree/rank fallback
- color grouping:
  - PD#PN nodes colored by prefix-derived palette
  - concept nodes in dedicated concept palette
- edge low-opacity baseline, stronger when related to active node
- label clutter control (selected/hovered/top-ranked emphasis)
- detail panel fields:
  - id
  - label
  - rank
  - PageRank/Gravity
  - in/out degree
  - connected edge count
  - source type

## Graph Counts and Default Mode

- Full PD#PN nodes: 747
- Full PD#PN edges: 7217
- Concept nodes: 11
- Concept edges: 21
- Paths: 3
- Default render mode: PD#PN Top 260

## Performance Notes

- Full graph mode is marked experimental.
- Top-N controls (100/260/500/all) limit load by default.
- Pair-force calculations are capped for larger node sets to avoid instability.

## How To Open

Open `browser-demo/index.html` directly in a local browser with file-path mode.

## Safety Scan Result

- No forbidden credential/secret patterns found.
- No SQL or backup pattern leaks found.
- No external web dependency references in browser demo files.
- No absolute local path leaks in browser-visible HTML/JS/CSS.

## Do-Not-Touch Confirmation

- Production touched: no
- Published touched: no
- Fixtures modified: no
- Copied seed files modified: no
- Old Zibaldone scripts executed: no
- Builds/pipelines/provider/API/LLM/network calls: no
