# AXIS-Cosmos Public Metadata and License Review 20260520

## Purpose

Polish public-facing repository metadata and document current license decision status without changing deployment posture.

## Current Repository Metadata

- Repository URL: `https://github.com/matikamata/axis-cosmos`
- Visibility: `PUBLIC`
- Default branch: `main`
- Deploy status: none configured

## License Status

Pending operator decision.

Public visibility does not imply doctrinal/content relicensing.

## Recommended License Options (No Auto-Selection)

- MIT (permissive)
- Apache-2.0 (permissive with patent grant)
- CC BY-NC-SA (content/docs-oriented, non-commercial; policy fit must be confirmed)
- Dual model (code license + separate content/doc terms), if needed by operator policy

## Suggested GitHub Metadata

- Description:
  - `Local-first AXIS-Cosmos graph/constellation lab for derived, non-canonical AXIS preservation archaeology.`
- Topics:
  - `axis`
  - `axis-cosmos`
  - `digital-preservation`
  - `graph-visualization`
  - `static-site`
  - `local-first`
  - `dhamma-dana`
  - `archive`
  - `knowledge-graph`

## Public-Safety Scan Summary

Verdict: **GO-with-WARN**.

- FAIL: none found.
- WARN:
  - Historical rescue/phase docs and generated reports still contain local absolute paths as archival context.
  - Safety-pattern keywords (for example `API_KEY`, `SECRET`, `TOKEN`) appear in checklists/scanners as policy text, not secrets.
- PASS:
  - No raw SQL/backup files found in repository tree.
  - No external `http://`/`https://` dependencies detected in `browser-demo/` runtime files.
  - Root `README.md` and `browser-demo/README.md` do not expose `/home/sanghop/` paths.

## Files Modified In This Batch

- `docs/PUBLIC_METADATA_AND_LICENSE_REVIEW_20260520.md` (created)

## Do-Not-Touch Confirmation

- Production touched: no.
- Published touched: no.
- Fixtures/seeds modified: no.
- Old Zibaldone scripts executed: no.
- Builds/pipelines/provider/API/LLM calls: no.
- Deploy configured: no.
