# Grafo_Constelacoes.json Review

## 1. Candidate

- Candidate name: `Grafo_Constelacoes.json`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/metadados/Grafo_Constelacoes.json`
- Intended future destination: `fixtures/zibaldone/sample_Grafo_Constelacoes.json`
- Candidate class: `LARGE_FIXTURE_SAMPLE_ONLY`
- Review status: reviewed / sample-only later
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: JSON text data
- Byte size: 1069633 bytes
- Line count: 41613 lines
- Valid JSON? yes
- Short structure summary: D3-style graph with top-level `nodes` and `links`; 789 nodes and 7217 links.
- Appears generated, handwritten, or curated fixture: generated D3 constellation fixture.

## 3. Provenance

This is a generated Zibaldone constellation artifact derived from the old graph extraction and rendering path. It is not Canon. It should not be copied whole initially.

## 4. Safety Scan Results

Forbidden-pattern scan result: clean. No matches for raw SQL names, WordPress config, credential/API/token strings, local absolute paths, `.git`, `.venv`, `.netlify`, `node_modules`, cache, or AppleDouble patterns.

## 5. Risk Assessment

Risks: large generated JSON; SQL-derived lineage; includes public URLs and graph visualization assumptions; should be sampled and labeled before entering git.

## 6. Copy Recommendation

Copy only as a trimmed sample later after operator approval and a documented sampling method. Do not copy the full file now.

## 7. Required Label If Copied Later

“This sample is derived from a larger Zibaldone D3 constellation artifact. It is not AXIS-NIDDHI Canon and is preserved only as a sanitized schema-shape sample.”

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
