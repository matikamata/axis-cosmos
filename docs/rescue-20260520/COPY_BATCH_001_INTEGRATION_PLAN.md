# COPY_BATCH_001 Integration Plan

## 1. Purpose

This document connects the first copied AXIS-Cosmos seed materials into a future integration path without creating code.

It explains how the copied artifacts should be interpreted, connected, validated, and eventually used before any validator, extractor, analyzer, renderer, or UI work begins.

## 2. Current Lab State

- `axis-cosmos-lab` is local-only.
- It is not a git repo.
- It has no deployment target.
- It has no production/published impact.
- COPY_BATCH_001 is completed.
- The copied artifacts are derived and non-canonical.

AXIS-NIDDHI Canon/CSL remains the source of truth. These files are seed material for planning, validation, and future tests only.

## 3. Copied Seed Roles

| File | Role | Type | Canon status | Future use | Risk / caveat |
|---|---|---|---|---|---|
| `docs/rescue-20260520/Grafo_Conexoes_Report.md` | Human-readable archaeology report | Markdown report | Not Canon; derived from old extraction | Explain graph scale, top sources/targets, and unknown slug evidence | SQL-derived; useful as evidence, not source of truth |
| `cosmos/schemas/graph_schema.json` | Early shared Navigator/Cosmos graph schema candidate | JSON schema-like contract | Not Canon; experimental | Seed future schema discussion for concept graph fixtures | Byte-identical to Navigator schema; ownership boundary required |
| `fixtures/zibaldone/cosmos_graph.json` | Small concept graph fixture | JSON fixture | Not Canon; derived sample | Test schema shape and concept graph assumptions later | Concept assumptions may be stale; Navigator overlap |
| `fixtures/zibaldone/cosmos_paths.json` | Small path fixture | JSON fixture | Not Canon; derived sample | Test graph/path compatibility later | Navigator overlap; path semantics need review |
| `fixtures/zibaldone/Grafo_Metricas.csv` | SQL-derived graph metric fixture | CSV fixture | Not Canon; derived metrics | Validate PageRank/in-degree/out-degree handling later | Metrics reflect old SQL-dependent extraction |
| `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv` | SQL-derived PD#PN edge-list fixture | CSV fixture | Not Canon; derived edge list | Validate post-link topology handling later | SQL-derived; must be rewritten from CSL/static indexes later |

## 4. Two Graph Worlds

### A. Concept / Navigator-style graph

Files:

- `graph_schema.json`
- `cosmos_graph.json`
- `cosmos_paths.json`

This world is concept-oriented. It uses concept IDs, concept nodes, concept edges, clusters, and named paths. It is useful for Navigator compatibility and future Nana/Academy concept navigation.

### B. PD#PN / post-link graph

Files:

- `Grafo_Conexoes_PDPN.csv`
- `Grafo_Metricas.csv`
- `Grafo_Conexoes_Report.md`

This world is post-link-oriented. It uses PD#PN source/target relationships, graph metrics, top source/target evidence, and unknown slug evidence.

The integration challenge is to bridge these worlds without confusing them. Concept graph fixtures should not be treated as post-link graphs, and PD#PN graph artifacts should not be treated as canonical concept maps.

## 5. Boundary Decisions

- The concept graph remains compatible with Navigator, but Cosmos may use copied local fixtures for planning and validation.
- The PD#PN graph remains SQL-derived archaeology until rewritten from CSL/static indexes.
- None of these files are Canon.
- Future code must treat all copied fixtures as derived test/sample data.
- `graph_schema.json` should not be accepted blindly as the final Cosmos schema; it should be compared against the broader `GraphBundle`, `Node`, `Edge`, `Path`, `Metric`, `Provenance`, and `SafetyReview` direction from `COSMOS_SCHEMA_NOTES.md`.

## 6. Future Validation Needs

Future validation should cover:

- JSON schema shape validation;
- CSV column validation;
- PD#PN format validation;
- node/edge consistency check;
- graph metric consistency check;
- concept/path compatibility check;
- provenance check;
- forbidden-pattern scan repeat.

Validation must be read-only first and should report findings before any transformation or generated output exists.

## 7. Future Module Plan

Future module ideas only:

- `cosmos.schemas`
  - Holds accepted schema contracts and schema documentation.
- `cosmos.validators`
  - Validates copied fixtures, schema shape, CSV columns, PD#PN formats, provenance, and forbidden patterns.
- `cosmos.extractors`
  - Eventually rewrites old extraction logic against CSL/static metadata, not raw SQL or WordPress backups.
- `cosmos.analyzers`
  - Computes derived graph metrics such as PageRank, in-degree, out-degree, hub scores, orphan checks, and unknown slug counts.
- `cosmos.renderers`
  - Exports graph data for visualization only after schema and validation are stable.

No module files are created by this plan.

## 8. Suggested Next Implementation Order

No implementation now. Recommended order:

1. Create docs-only validation spec.
2. Create minimal read-only validator design.
3. Add tiny test fixtures or use copied fixtures read-only.
4. Write pure validation functions.
5. Only later rewrite extractors.
6. Only much later build renderers/UI.

## 9. Do Not Touch / Deferred Items

- `Grafo_Constelacoes.json`: sample-only later.
- `index.html`: UI archaeology docs only.
- `learning_paths.json`: boundary pending.
- `study_paths.json`: boundary pending.
- Old scripts: rewrite only, never execute or copy blindly.
- Raw SQL, backups, and credentials: forbidden.

## 10. Next Safe Step

Create `VALIDATION_SPEC.md` as a docs-only validation contract before writing any validator code.

## 11. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COPY_BATCH_001_INTEGRATION_PLAN.md`; updated `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COSMOS_OPERATOR_DASHBOARD.md`.
- Production touched: no.
- Published touched: no.
- More Zibaldone files copied: no.
- Code or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
