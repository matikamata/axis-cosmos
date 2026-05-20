# Remote Repo Alignment

## 1. Purpose

This document defines repo boundaries before AXIS-Cosmos absorbs any material from Zibaldone, Navigator, Nana, CLI, Mirror, or Preservation.

It is a docs-only planning note. It does not copy fixtures, create schemas, create code, initialize git, fetch remotes, or change any deployment surface.

## 2. Known Public Repos

| Repo | Public exists? | Local path observed | Role | Cosmos relationship | Boundary decision |
|---|---|---|---|---|---|
| `axis-niddhi` | yes, known public repo | `/home/sanghop/axis/axis-niddhi-production` | Canon/pipeline/deployment source for AXIS-NIDDHI | Upstream source of CSL/static metadata, PD#PN identity, titles, and safe indexes | Cosmos may consume sanitized derived metadata later; Cosmos must never mutate Canon or Niddhi pipeline files |
| `axis-nana` | yes, known public repo | `/home/sanghop/axis/axis-nana-lab` | Source-bound concept/reasoning lab | Provides concept-map hints, source-bound concept IDs, and possible graph hints | Nana engine/provider logic stays in Nana; Cosmos may consume sanitized concept hints later |
| `axis-navigator` | yes, known public repo | `/home/sanghop/axis/axis-navigator-lab` | Reader/study overlay and navigation lab | Provides path schemas, graph schema ideas, study paths, and reader context | Navigator UI/overlay remains in Navigator; Cosmos may own derived graph topology and renderer experiments |
| `axis-cli` | yes, known public repo | `/home/sanghop/bengyond-playground/axis-cli` | Local cockpit and command surface | May eventually call Cosmos tools after they exist | Shell cockpit/orchestrator scripts do not belong in Cosmos; Cosmos may document future CLI requirements only |
| `axis-mirror` | yes, known public repo | `/home/sanghop/bengyond-playground/axis-mirror` | Mirror/sync/distribution experiments | Possible future distribution channel for sanitized Cosmos artifacts | Mirror sync logic and configs stay out of Cosmos |
| `axis-preservation` | yes, known public repo | `/home/sanghop/bengyond-playground/axis-preservation` | Ledger/seal/preservation records | Possible future verification layer for released Cosmos artifacts | Ledger/seal scripts and artifacts stay in Preservation unless explicitly redesigned |
| future `axis-cosmos` | no public repo yet | `/home/sanghop/axis/axis-cosmos-lab` | Local-only graph, constellation, relationship, and study-path lab | Owns derived graph contracts, sanitized fixtures, analyzers, renderers, and source maps | Remain local-only until docs, fixtures, schema, and source boundaries are stable |

## 3. Cosmos Boundary

Belongs in Cosmos:

- graph schema contracts;
- sanitized graph fixtures;
- graph analyzers;
- graph renderers;
- source maps;
- post-link topology;
- concept/study graph topology;
- relationship visualization planning.

Does not belong in Cosmos:

- Canon/CSL mutation;
- Niddhi pipeline;
- Nana provider execution;
- Navigator reader overlay UI;
- CLI cockpit;
- Mirror sync;
- Preservation ledger/seal;
- raw SQL;
- WordPress backup material;
- deployment config.

## 4. Cross-Repo Interfaces

Safe future interfaces:

- From Niddhi: CSL/static metadata, PD#PN identifiers, post titles, and safe indexes.
- From Nana: concept-map hints, source-bound concept IDs, and graph hints.
- From Navigator: graph/path schemas, study paths, and reader context.
- To Academy/sKullApp/PitiPath: sanitized `GraphBundle`, `StudyPath`, and `ConceptHint` outputs.
- To CLI: future command requirements only, not inherited shell scripts.
- To Preservation/Mirror: optional artifact verification or distribution later, not part of this local-only stage.

## 5. Redirection Rules

| Material | Belongs to | Why | Cosmos action |
|---|---|---|---|
| `axis_cli.sh` | `axis-cli` | It is cockpit/orchestration behavior, not graph domain logic | Document future command needs only; do not copy script into Cosmos |
| mirror sync scripts/configs | `axis-mirror` | Sync/distribution is a mirror concern | Keep out of Cosmos; reference only if artifact distribution becomes relevant later |
| ledger/seal scripts/artifacts | `axis-preservation` | Integrity, sealing, and preservation records belong to the preservation layer | Keep out of Cosmos; define possible verification interface later |
| provider/Gemini/Vertex scripts | `axis-nana` or provider-specific labs | Provider execution is not Cosmos responsibility and may touch external services | Do not copy or execute; keep Cosmos provider-free |
| Navigator overlay JS/CSS | `axis-navigator` | Reader overlay UX belongs to Navigator | Cosmos may document graph renderer needs, but should not absorb the reader overlay |
| Nana engine/provider files | `axis-nana` | Nana owns source-bound reasoning and provider-safe wrappers | Cosmos may consume sanitized concept hints only |
| graph schema/fixtures | `axis-cosmos-lab` after review | Derived graph contracts and sanitized examples are Cosmos core material | Candidate for future sanitized docs/fixtures/schema pass |
| learning/study paths | Cosmos plus Navigator/Academy boundary | Paths can feed graph topology, reader UX, and future learning surfaces | Keep schema boundary explicit; copy only sanitized samples later |
| raw SQL and WordPress backups | nowhere in Cosmos git | Raw backups are unsafe, oversized, and not aligned with Canon-first architecture | Quarantine outside Cosmos; document archaeology only |

## 6. Local-Only Policy

`axis-cosmos-lab` remains local-only for now.

There is no public Cosmos repo yet, no git initialization, and no deploy target. A public repo may be considered later only after sanitized docs, fixtures, and schema contracts are stable, and after forbidden input boundaries are confirmed.

## 7. Next Safe Step

Create a fixture sanitization checklist next.

That is safer than drafting a fixture manifest first because it defines the safety gates before naming anything as copy-ready. The checklist should cover file size, forbidden paths, credential-like strings, raw SQL exclusion, generated-vs-source classification, and public-safety decisions.

## 8. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/REMOTE_REPO_ALIGNMENT.md`.
- Production touched: no.
- Published touched: no.
- Zibaldone files copied: no.
- Schemas, fixtures, code folders, or scripts created: no.
- Git initialized: no.
- Clone/fetch/commit/push/deploy happened: no.
- Builds, pipelines, scripts, or provider calls ran: no.
