# AXIS-Cosmos Lab

## Status

AXIS-Cosmos Lab is a local-only preservation and archaeology lab. It is not a deployment surface, not part of `axis-niddhi-production`, not part of `axis-niddhi-published`, and not allowed to mutate Canon.

The future local path is expected to be:

```text
/home/sanghop/axis/axis-cosmos-lab
```

That directory now exists as a local-only lab workspace and contains docs, reviewed copied rescue fixtures, read-only validator/analyzer scripts, local analysis/validation outputs, and a browser demo.

Quick start browser demo:

- Open `browser-demo/index.html` directly in a browser (`file://`).
- Demo is derived/non-canonical and local-only.
- No deploy target and no production connection.

## Purpose

AXIS-Cosmos explores graph, constellation, relationship, study-path, and concept-navigation views derived from safe AXIS artifacts. It is intended to help inspect relationships among canonical PureDhamma entries, PD#PN links, Pali concepts, study paths, semantic clusters, graph hubs, prerequisite chains, and future learning surfaces without changing Canon or production output.

## Architectural Position

```text
AXIS-NIDDHI / Canon
  -> AXIS-Nana / source-bound concepts
  -> AXIS-Navigator / reader/study overlay
  -> AXIS-Cosmos / graph + paths + relationships
  -> future Academy / sKullApp / PitiPath
```

Cosmos consumes canonical or sanitized derived artifacts. It never edits Canon, rewrites CSL, deploys pages, runs providers, or replaces AXIS-NIDDHI, AXIS-Nana, or AXIS-Navigator.

## Safety Rules

- No raw SQL.
- No WordPress backups.
- No credentials or local API/provider secrets.
- No `.git`, `.venv`, `.netlify`, or `node_modules`.
- No `__pycache__`, `*.pyc`, or AppleDouble `._*` files.
- No generated static-site trees.
- No provider/API/LLM execution.
- No old shell orchestrators.
- No production or published writes.
- No deploy targets until the lab boundary is stable.

## Initial Scope

Allowed first-pass contents:

- docs;
- sanitized fixtures;
- schemas;
- archaeology notes;
- small sample graph files;
- source maps;
- future rewritten/pure extractor designs;
- future rewritten/pure analyzer designs.

Implementation code is deferred until the source boundary, fixture policy, and schema contract are clear.

## Seed Materials

Planned first seed materials:

1. `Grafo_Conexoes_Report.md`
2. `Grafo_Metricas.csv`
3. `Grafo_Conexoes_PDPN.csv`
4. `Grafo_Constelacoes.json` as sample/trim candidate
5. `index.html` as UI archaeology
6. `graph_schema.json`
7. `cosmos_graph.json`
8. `cosmos_paths.json`
9. `learning_paths.json`
10. `study_paths.json`

These began as candidate seeds. Controlled COPY_BATCH_001 moved a reviewed subset into the lab with provenance and read-only validation context; remaining candidates stayed deferred.

## Old Script Policy

The following are archaeology:

- `ligue_os_pontos.py`
- `gerar_json_d3.py`
- `analisar_grafo.py`
- `cosmos_engine.py`
- `graph_builder.py`

They must not be executed blindly. They must be rewritten, isolated, or converted into documented design notes before becoming Cosmos code.

`axis_cli.sh` belongs to `axis-cli`, not Cosmos. Mirror, capsule, ledger, deploy, provider, API, and LLM wrappers are routed out of Cosmos.

## Proposed Future Tree

Proposal only:

```text
axis-cosmos-lab/
  README.md
  docs/
    rescue-20260520/
  fixtures/
    zibaldone/
  cosmos/
    schemas/
    extractors/
    analyzers/
    renderers/
  scripts/
    README.md
```

## First Mile Plan

No implementation yet.

1. Accept the Cosmos charter.
2. Create the empty local-only lab.
3. Add this README as `README.md`.
4. Add `docs/rescue-20260520/`.
5. Copy only selected docs/fixtures after sanitization.
6. Write `ZIBALDONE_COSMOS_SOURCE_MAP.md`.
7. Defer code until extractors/analyzers can be pure, read-only, and tested.

## Do Not Touch Confirmation

Files created/modified:

- Created the initial local-only docs skeleton:
  - `/home/sanghop/axis/axis-cosmos-lab/`
  - `/home/sanghop/axis/axis-cosmos-lab/README.md`
  - `/home/sanghop/axis/axis-cosmos-lab/docs/`
  - `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/`
  - `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/README.md`

Protected paths:

- `/home/sanghop/axis/axis-niddhi-production`: not touched.
- `/home/sanghop/axis/axis-niddhi-published`: not touched.

Lab creation:

- `/home/sanghop/axis/axis-cosmos-lab`: created as a local-only docs skeleton.

Execution safety:

- No builds were run.
- No pipelines were run.
- No Zibaldone scripts were executed.
- No provider/API/LLM calls were run.
- No packages were installed.
- No repos were cloned.
- No commits were made.
- No pushes were made.
- No deploys were made.
- Initial pass copied no files from Zibaldone; later approved rescue batches copied a reviewed subset with provenance tracking.
- Initial pass created no fixtures/schemas/scripts/code folders; later approved rescue batches introduced controlled local-only artifacts and read-only scripts.
