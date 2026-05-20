# Grafo_Conexoes_Report.md Review

## 1. Candidate

- Candidate name: `Grafo_Conexoes_Report.md`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_Report.md`
- Intended future destination: `docs/rescue-20260520/` or `docs/rescue-20260520/fixture-reviews/`
- Candidate class: `DOC_SAFE_CANDIDATE`
- Review status: reviewed / pending operator approval
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: Unicode text, UTF-8 text
- Byte size: 3277 bytes
- Line count: 67 lines
- Short content summary: generated AXIS-Cosmos graph connection report with graph summary counts, top source posts, top target posts, and unknown slug counts.
- Appears generated or handwritten: generated report

## 3. Provenance

This appears to be a generated report from Zibaldone Cosmos graph archaeology.

It is derived from the old SQL-dependent extraction flow:

raw WordPress SQL and MasterPDPN-style metadata -> PD#PN link extraction -> graph summary and unknown slug reporting.

It is not Canon. If copied later, it must be labeled as a derived archaeology artifact and not treated as AXIS-NIDDHI Canon or current source-of-truth metadata.

## 4. Safety Scan Results

Scan command used: forbidden-pattern `rg` over the candidate file only.

| Pattern | Found? | Notes |
|---|---|---|
| `tenweb_backup_db.sql` | no | No match. |
| `wp-config.php` | no | No match. |
| `DB_PASSWORD` | no | No match. |
| `GOOGLE_APPLICATION_CREDENTIALS` | no | No match. |
| `DEEPL` | no | No match. |
| `API_KEY` | no | No match. |
| `SECRET` | no | No match. |
| `TOKEN` | no | No match. |
| `/home/sanghop/` | no | No local absolute path match. |
| `/media/sanghop/` | no | No local media path match. |
| `.git/` | no | No match. |
| `.venv` | no | No match. |
| `.netlify` | no | No match. |
| `node_modules` | no | No match. |
| `__pycache__` | no | No match. |
| `._` | no | No AppleDouble-style match. |

No local path references were found in the candidate during this scan.

## 5. Content Value

This report is useful because it preserves:

- graph summary counts;
- node and edge scale evidence;
- source-to-target relationship evidence;
- unknown slug evidence;
- seed context for the Cosmos source map and future validation work.

It is especially useful as a lightweight archaeology artifact because it is small and human-readable, unlike the larger graph JSON outputs.

## 6. Risk Assessment

Risks:

- SQL-derived provenance means it reflects an old extraction path, not the current Canon-first architecture.
- Generated-report status means it should be treated as evidence, not source.
- It may encode old assumptions about PD#PN mapping, slug resolution, and WordPress extraction behavior.
- It is not canonical truth.
- If copied later, it needs a derived-artifact label.

No forbidden strings or local absolute path references were found in this review pass.

## 7. Recommendation

Safe to copy later after operator approval, if this review is accepted.

Do not copy it now.

## 8. Required Label If Copied Later

“This file is a derived Zibaldone archaeology report. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path. It is preserved only as historical Cosmos evidence.”

## 9. Next Safe Step

Create the next review note for `graph_schema.json`, because schema-like material is likely safer than CSV, large JSON, or old HTML.

Do not create it in this pass.

## 10. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/fixture-reviews/Grafo_Conexoes_Report_REVIEW.md`.
- Production touched: no.
- Published touched: no.
- Candidate copied: no.
- Zibaldone files copied: no.
- Schemas, code folders, or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
