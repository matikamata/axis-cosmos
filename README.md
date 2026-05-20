# AXIS-Cosmos

Local-first graph/constellation layer for AXIS preservation research.

## Status

Experimental, derived, non-canonical research lab.

- Not Canon.
- Not a deploy surface.
- Not connected to production or published pipelines.

## Position In AXIS

```text
AXIS-NIDDHI (Canon/CSL authority)
  -> AXIS-NANA (concept hints)
  -> AXIS-Navigator (reader/path overlays)
  -> AXIS-Cosmos (graph/path archaeology + local visualization)
```

CSL, identity records, lineage records, and future validated graph outputs remain authoritative.

## Local Demo

Open:

- `browser-demo/index.html`

No build step, no server required, no external CDN dependencies.

## Safety Boundary

- Local-only research workflow.
- No provider/API/LLM calls in repo workflows.
- No external browser dependencies.
- Copied fixtures are derived archaeology samples.
- No production/published writes from this repository.
- No deploy target configured.

## Path Convention

Use placeholders in docs and examples:

- `<AXIS_ROOT>`: local workspace root (example: parent directory containing `axis-cosmos`)
- `<AXIS_ROOT>/axis-cosmos`: local repository path

## Repository Layout

```text
axis-cosmos/
  browser-demo/   # local interactive universe demo
  cosmos/         # schema area
  docs/           # rescue, phase, and release records
  fixtures/       # reviewed derived fixtures
  outputs/        # validation/analysis outputs
  scripts/        # read-only validator/analyzer tools
```

## License

Pending operator decision.

Public visibility of this repository does not imply doctrinal/content relicensing.
