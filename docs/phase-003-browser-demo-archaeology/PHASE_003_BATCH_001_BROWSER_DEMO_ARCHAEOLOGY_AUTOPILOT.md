# PHASE 003 Batch 001 Browser Demo Archaeology Autopilot

## Purpose

Run a local-only browser archaeology cycle to recover useful Cosmos visual behavior safely, without using old scripts or touching protected environments.

## Old UI Files Inspected

- `Zibaldone_20260519_22h22/index.html` (legacy root copy)
- `The-Skunkworks-Sublime-Saga/index.html` under legacy playground tree (not found)
- Nearby Skunkworks browser pages were inspected read-only as context.

## Direct Copy Decision

Old UI was not copied directly.

Reasons:
- External dependency found (`d3.v7.min.js` from CDN).
- Server-oriented usage assumptions.
- Not aligned with local-only no-network constraint.

## Created Local Demo Files

- `browser-demo/README.md`
- `browser-demo/index.html`
- `browser-demo/style.css`
- `browser-demo/demo.js`

## Data Source Used

Tiny embedded sample shaped from already copied local fixtures:

- `fixtures/zibaldone/cosmos_graph.json`
- `fixtures/zibaldone/cosmos_paths.json`
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`

No copied seed file was edited.

## Safety Scan Result

- No protected path references found.
- No credential-like tokens found.
- No SQL or backup indicators found.
- No external `http` or `https` dependencies found in created demo files.

## How To Open Locally

Open `browser-demo/index.html` directly in a local browser.

## Known Limitations

- This is a minimal archaeology demo, not full historical parity.
- Uses embedded sample data rather than dynamic file loading.
- Not canonical and not a replacement for validated outputs.

## Recommended Next Action

Run a docs-only review pass for Phase 003 Batch 001 and decide whether to keep this demo frozen or approve a tightly scoped Phase 003 Batch 002 for safe incremental visualization improvements.

## Do Not Touch Confirmation

- Production touched: no.
- Published touched: no.
- Fixtures modified: no.
- Copied seeds modified: no.
- Scripts executed from old Zibaldone: no.
- Builds/pipelines/provider/API/LLM/network calls: no.
