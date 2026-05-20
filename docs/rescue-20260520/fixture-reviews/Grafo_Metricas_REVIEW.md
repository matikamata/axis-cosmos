# Grafo_Metricas.csv Review

## 1. Candidate

- Candidate name: `Grafo_Metricas.csv`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Metricas.csv`
- Intended future destination: `fixtures/zibaldone/Grafo_Metricas.csv`
- Candidate class: `SMALL_FIXTURE_CANDIDATE`
- Review status: reviewed / pending operator approval
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: ASCII text, CRLF line terminators
- Byte size: 28115 bytes
- Line count: 748 lines
- Valid CSV? yes, semicolon-delimited with consistent 4-field rows
- Short structure summary: graph metric table with columns `PD#PN`, `PageRank`, `InDegree`, and `OutDegree`.
- Appears generated, handwritten, or curated fixture: generated metrics fixture.

## 3. Provenance

This is a Zibaldone graph-metrics output derived from the old SQL-dependent extraction and analysis flow. It is not Canon. If copied later, it must be labeled as derived graph archaeology.

## 4. Safety Scan Results

Forbidden-pattern scan result: clean. No matches for raw SQL names, WordPress config, credential/API/token strings, local absolute paths, `.git`, `.venv`, `.netlify`, `node_modules`, cache, or AppleDouble patterns.

## 5. Risk Assessment

Risks: SQL-derived provenance; generated metrics may reflect stale source state; PageRank/degree values are derived observations, not canonical metadata.

## 6. Copy Recommendation

Safe to copy later after operator approval and provenance label. Do not copy now.

## 7. Required Label If Copied Later

“This CSV is a derived Zibaldone graph-metrics artifact. It is not AXIS-NIDDHI Canon and was generated from an older SQL-dependent extraction path.”

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
