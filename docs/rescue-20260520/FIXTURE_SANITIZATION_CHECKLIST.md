# Fixture Sanitization Checklist

## 1. Purpose

This checklist must be applied before any Zibaldone fixture, schema, report, or UI artifact is copied into AXIS-Cosmos.

It is a docs-only safety gate. It defines review requirements before any migration, sampling, schema creation, fixture creation, or executable code exists in the lab.

## 2. Sanitization Principle

- No fixture enters Cosmos by default.
- Every candidate must pass review.
- Copied files must be sanitized, small enough, provenance-labeled, and non-canonical.
- Derived artifacts must never be confused with Canon.

Cosmos may preserve derived graph knowledge, but AXIS-NIDDHI Canon/CSL remains the source of truth.

## 3. Candidate Classes

| Class | Meaning | Default action |
|---|---|---|
| `DOC_SAFE_CANDIDATE` | Documentation, reports, source maps, or design notes with no sensitive source material | Review, then copy later if provenance is clear |
| `SCHEMA_SAFE_CANDIDATE` | JSON schema or schema-like contract material | Review structure and ownership before copying |
| `SMALL_FIXTURE_CANDIDATE` | Small sanitized sample data useful for tests or docs | Review content, provenance, and public-safety before copying |
| `LARGE_FIXTURE_SAMPLE_ONLY` | Large generated output that should not enter the lab whole | Record original location and create a trimmed sample later |
| `UI_ARCHAEOLOGY_DOC_ONLY` | Old prototype UI, HTML, CSS, or JS useful as design reference | Document behavior; do not copy as executable UI yet |
| `SCRIPT_ARCHAEOLOGY_DOC_ONLY` | Old scripts useful for understanding extraction or analysis | Document roles and rewrite direction; do not copy into executable paths |
| `FORBIDDEN_DO_NOT_COPY` | Raw SQL, backups, credentials, caches, generated static trees, or unsafe artifacts | Do not copy |
| `CROSS_REPO_REDIRECT` | Material that belongs in Nana, Navigator, CLI, Mirror, Preservation, or Niddhi docs | Record boundary and route later |

## 4. Mandatory Checks

Before any candidate is copied later:

- [ ] Source path recorded.
- [ ] Intended destination recorded.
- [ ] Class assigned.
- [ ] File size checked.
- [ ] File type checked.
- [ ] Provenance recorded.
- [ ] Source-vs-generated classification completed.
- [ ] Raw SQL exclusion confirmed.
- [ ] WordPress backup exclusion confirmed.
- [ ] Credential-like string scan completed.
- [ ] Forbidden path string scan completed.
- [ ] Local absolute path scan completed.
- [ ] API/provider token scan completed.
- [ ] `.git` / `.venv` / `.netlify` / `node_modules` exclusion confirmed.
- [ ] pyc/cache/AppleDouble exclusion confirmed.
- [ ] Generated static-site tree exclusion confirmed.
- [ ] Public-safety decision recorded.
- [ ] Copy decision recorded.
- [ ] Reviewer/date note recorded.

## 5. Forbidden Strings and Patterns

Examples to scan for:

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

A path reference in documentation may be acceptable if it is intentional archaeology context. Credentials, raw source material, backup contents, provider tokens, and executable access paths are not acceptable fixture content.

## 6. First Seed Review Matrix

| Seed | Current class | Expected destination | Must check before copy | Likely decision |
|---|---|---|---|---|
| `Grafo_Conexoes_Report.md` | `DOC_SAFE_CANDIDATE` | `docs/rescue-20260520/` or future fixture notes | Provenance, local absolute paths, generated-source labeling | Copy later after review |
| `Grafo_Metricas.csv` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/Grafo_Metricas.csv` later | Size, column meaning, SQL-derived provenance, public-safety scan | Copy later if small and clean |
| `Grafo_Conexoes_PDPN.csv` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv` later | Size, PD#PN relation semantics, SQL-derived provenance, unknown slug exposure | Copy later if sanitized |
| `Grafo_Constelacoes.json` | `LARGE_FIXTURE_SAMPLE_ONLY` | `fixtures/zibaldone/sample_Grafo_Constelacoes.json` later | Size, forbidden strings, sampling strategy, schema shape preservation | Trim/sample later, not whole initially |
| `index.html` | `UI_ARCHAEOLOGY_DOC_ONLY` | Future `docs/rescue-20260520/COSMOS_UI_ARCHAEOLOGY.md` or renderer notes | External dependencies, embedded data, executable behavior, local paths | Document first; do not copy as runnable UI yet |
| `graph_schema.json` | `SCHEMA_SAFE_CANDIDATE` | Future `cosmos/schemas/graph_schema.json` after acceptance | Compatibility with Navigator schema, required fields, provenance fields | Copy later only after schema decision |
| `cosmos_graph.json` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/cosmos_graph.json` later | Size, schema match, stale assumptions, public-safety scan | Copy later if clean |
| `cosmos_paths.json` | `SMALL_FIXTURE_CANDIDATE` | `fixtures/zibaldone/cosmos_paths.json` later | Path schema compatibility, Navigator overlap, provenance | Copy later if boundary is clear |
| `learning_paths.json` | `CROSS_REPO_REDIRECT` | Cosmos fixture or Navigator/Academy notes after boundary review | Ownership, schema overlap, public-safety scan | Copy later only with boundary note |
| `study_paths.json` | `CROSS_REPO_REDIRECT` | Cosmos fixture or Navigator/Academy notes after boundary review | Ownership, schema overlap, public-safety scan | Copy later only with boundary note |

No seed is copied in this pass.

## 7. Large Fixture Policy

- Large JSON should not be copied as-is initially.
- Prefer trimmed samples.
- Record original size.
- Record sampling method later.
- Generated samples must preserve schema shape but not require full corpus scale.

A sample is acceptable only when it is small, sanitized, provenance-labeled, and clearly marked as derived.

## 8. Script Handling Policy

- Scripts are not fixtures.
- Old scripts remain docs-only archaeology.
- No old script is copied into executable paths.
- Future code must be rewritten as pure functions with tests.

The old SQL-dependent extraction scripts are useful as historical design evidence, not as current implementation.

## 9. Copy-Ready Definition

A file is copy-ready only if:

- class is safe;
- no forbidden material found;
- destination is clear;
- provenance note exists;
- size is acceptable or sample policy exists;
- reviewed by operator;
- no production/published impact.

Until all of those are true, the candidate remains mapped but not copied.

## 10. Next Safe Step

Create `FIXTURE_MANIFEST_DRAFT.md` after this checklist.

That draft should list candidate files, intended future destinations, class, review status, and copy decision without copying any seed material.

## 11. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/FIXTURE_SANITIZATION_CHECKLIST.md`.
- Production touched: no.
- Published touched: no.
- Zibaldone files copied: no.
- Schemas, fixtures, code folders, or scripts created: no.
- Git initialized: no.
- Clone/fetch/commit/push/deploy happened: no.
- Builds, pipelines, scripts, or provider calls ran: no.
