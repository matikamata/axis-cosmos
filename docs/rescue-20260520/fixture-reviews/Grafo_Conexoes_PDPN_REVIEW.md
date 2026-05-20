# Grafo_Conexoes_PDPN.csv Review

## 1. Candidate

- Candidate name: `Grafo_Conexoes_PDPN.csv`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Conexoes_PDPN.csv`
- Intended future destination: `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`
- Candidate class: `SMALL_FIXTURE_CANDIDATE`
- Review status: reviewed / pending operator approval
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: ASCII text, CRLF line terminators
- Byte size: 151527 bytes
- Line count: 7218 lines
- Valid CSV? yes, semicolon-delimited with consistent 2-field rows
- Short structure summary: PD#PN edge list with columns `Source` and `Target`; 7217 data rows.
- Appears generated, handwritten, or curated fixture: generated edge-list fixture.

## 3. Provenance

This is a Zibaldone PD#PN relationship output derived from the old SQL-dependent extraction flow. It is not Canon. It should be treated as relationship evidence, not source-of-truth content.

## 4. Safety Scan Results

Forbidden-pattern scan result: clean. No matches for raw SQL names, WordPress config, credential/API/token strings, local absolute paths, `.git`, `.venv`, `.netlify`, `node_modules`, cache, or AppleDouble patterns.

## 5. Risk Assessment

Risks: SQL-derived provenance; medium row count; possible stale internal-link assumptions; unknown slug resolution was handled elsewhere and should be revalidated before use.

## 6. Copy Recommendation

Safe to copy later after operator approval, provenance label, and a note that it is SQL-derived archaeology. Do not copy now.

## 7. Required Label If Copied Later

“This CSV is a derived Zibaldone PD#PN edge-list artifact. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path.”

## 8. Do Not Touch Confirmation

- Files created/modified: created this review note only.
- Production touched: no.
- Published touched: no.
- Candidate copied: no.
- Zibaldone files copied: no.
- Schemas, code folders, or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
