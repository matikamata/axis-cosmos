# cosmos_graph.json Review

## 1. Candidate

- Candidate name: `cosmos_graph.json`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/cosmos_graph.json`
- Intended future destination: `fixtures/zibaldone/cosmos_graph.json`
- Candidate class: `SMALL_FIXTURE_CANDIDATE`
- Review status: reviewed / pending operator approval
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: JSON text data
- Byte size: 7267 bytes
- Line count: 319 lines
- Valid JSON? yes
- Top-level keys: `clusters`, `edges`, `engine`, `generated`, `invariant`, `nodes`, `schema`, `stats`
- Short structure summary: small concept graph fixture with generation metadata, schema marker, nodes, edges, clusters, and stats.
- Appears generated, handwritten, or curated fixture: generated or curated fixture. It includes a `generated` timestamp and structured concept graph data.

## 3. Fixture Shape

Visible structure from limited inspection:

- Node-like records: yes, under `nodes`.
- Edge-like records: yes, under `edges`.
- Clusters: yes, under `clusters`.
- Paths: no top-level `paths` key observed in this file.
- Concept IDs: yes, examples include concept-style IDs such as `dukkha`, `anicca`, `anatta`, and `tilakkhana`.
- Relation types: yes, expected to align with `AXIS-COSMOS-GRAPH-V1` edge relation vocabulary.
- Compatibility with `graph_schema.json`: strong apparent compatibility. The fixture declares `schema: AXIS-COSMOS-GRAPH-V1` and uses concept node fields visible in the reviewed schema.

The full file was not copied or printed.

## 4. Comparison Results

| Comparison target | Exists? | Byte-identical? | SHA-256 | Boundary implication |
|---|---|---|---|---|
| `/home/sanghop/axis/axis-navigator-lab/navigator/cosmos_graph.json` | yes | yes | `5eb063c5e707d84ff60f0430f70097096d5f5f6f3a1efe97a4b4948ecc5f6590` | The candidate matches Navigator material, which is useful for compatibility but requires a Cosmos/Navigator boundary note. |
| Candidate source | yes | n/a | `5eb063c5e707d84ff60f0430f70097096d5f5f6f3a1efe97a4b4948ecc5f6590` | Candidate hash used as baseline. |

Because this fixture matches Navigator material, it should not be treated as purely Cosmos-owned without review. It is useful as a compatibility sample, but it is not Canon.

## 5. Provenance

This fixture comes from Skunkworks/Zibaldone archaeology and likely represents an early Cosmos/Navigator concept graph fixture.

It is not Canon. It is a derived and experimental fixture only. If copied later, it must be labeled as an archaeology sample and reviewed against the accepted Cosmos schema process.

## 6. Safety Scan Results

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

## 7. Content Value

This fixture is useful because it provides:

- a small concept graph sample;
- a possible test fixture for schema shape;
- a bridge between Navigator graph schema and future Cosmos `GraphBundle`;
- a safer review target than large D3 JSON.

It can help validate future schema, analyzer, and renderer expectations without requiring a full corpus-scale graph.

## 8. Risk Assessment

Risks:

- It is an old experimental fixture.
- It overlaps with Navigator ownership because it is byte-identical to `axis-navigator-lab/navigator/cosmos_graph.json`.
- Concept assumptions may be stale.
- It is not canonical truth.
- It should not be copied into `fixtures/zibaldone/` without operator approval and a provenance label.

## 9. Recommendation

Safe to copy later after operator approval and provenance label, if this review is accepted.

Do not copy it now.

## 10. Required Label If Copied Later

“This file is a derived Zibaldone/Skunkworks concept graph fixture. It is not AXIS-NIDDHI Canon and is preserved only as an experimental Cosmos/Navigator compatibility sample.”

## 11. Next Safe Step

Create the next review note for `cosmos_paths.json`, because it is the matching path fixture and helps validate graph/path compatibility.

Do not create it in this pass.

## 12. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/fixture-reviews/cosmos_graph_REVIEW.md`; modified `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/fixture-reviews/README.md`.
- Production touched: no.
- Published touched: no.
- Candidate copied: no.
- Zibaldone files copied: no.
- Schemas, code folders, or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
