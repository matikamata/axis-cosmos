# graph_schema.json Review

## 1. Candidate

- Candidate name: `graph_schema.json`
- Source path: `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/The-Skunkworks-Sublime-Saga/graph_schema.json`
- Intended future destination: `cosmos/schemas/graph_schema.json`
- Candidate class: `SCHEMA_SAFE_CANDIDATE`
- Review status: reviewed / pending operator approval
- Copy decision: not copied in this pass

## 2. File Inspection

- File exists? yes
- File type: JSON text data
- Byte size: 2706 bytes
- Line count: 53 lines
- Valid JSON? yes
- Short structure summary: top-level schema metadata with `schema`, `version`, `engine`, `description`, `invariant`, `node`, `edge`, `relation_types`, `clusters`, and `compatibility`.
- Appears schema-like, generated, or handwritten: schema-like and likely handwritten or curated, not a generated data fixture.

## 3. Schema Identity

Visible schema/version identifiers:

- `schema`: `AXIS-COSMOS-GRAPH-V1`
- `version`: `1.0`
- `engine`: `AXIS-NIDDHI`
- `description`: canonical knowledge graph schema for AXIS COSMOS

Visible field families:

- Node required fields: `concept_id`, `label`, `depth`
- Node optional fields: `citation_count`, `centrality_score`, `gravity_score`, `cluster_id`, `type`, `pali`
- Edge required fields: `source`, `target`
- Edge optional fields: `relation_type`, `weight`
- Relation types: `depends_on`, `co_occurs`, `path_sequence`, `causal`, `cessation`
- Cluster fields: `cluster_id`, `name`, `concepts`, `gravity_center`

The schema looks concept-oriented rather than post-link-oriented. It may still serve as a Cosmos seed because it defines concept graph objects and path-oriented relation types.

## 4. Comparison Results

| Comparison target | Exists? | Byte-identical? | SHA-256 | Boundary implication |
|---|---|---|---|---|
| `/home/sanghop/axis/axis-navigator-lab/navigator/graph_schema.json` | yes | yes | `c11c2c1547147f576d56e76829fade09110be634aebf204e962f7591b7e22a1d` | The candidate matches current Navigator schema, so Cosmos compatibility is strong but ownership must be explicit. |
| `/home/sanghop/axis/Zibaldone_20260519_22h22/bengyond-playground-to-organize/axis-navigator/navigator/graph_schema.json` | yes | yes | `c11c2c1547147f576d56e76829fade09110be634aebf204e962f7591b7e22a1d` | The candidate also matches the copied Navigator schema in Zibaldone, suggesting this schema traveled across Navigator and Skunkworks materials. |
| Candidate source | yes | n/a | `c11c2c1547147f576d56e76829fade09110be634aebf204e962f7591b7e22a1d` | Candidate hash used as baseline. |

If this schema matches Navigator, that is useful for compatibility. Cosmos should not blindly absorb Navigator ownership. Copying later requires a boundary note explaining whether the schema is shared, forked, or imported as archaeology.

## 5. Provenance

This schema comes from Skunkworks/Zibaldone archaeology and appears connected to an early Navigator/Cosmos graph contract.

It is not Canon. It is a schema candidate only, not an accepted Cosmos schema. If copied later, it should be labeled as derived/experimental and reviewed against the current Cosmos schema notes before any `cosmos/schemas/` path is created.

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

This schema is useful because it preserves:

- an early Cosmos graph contract;
- possible compatibility with Navigator graph/path data;
- seed structure for future `GraphBundle`, `Node`, `Edge`, and `Path` schema work;
- a small structural artifact that is safer to review than large fixture JSON or old HTML.

## 8. Risk Assessment

Risks:

- Ownership overlaps with Navigator because the candidate is byte-identical to `axis-navigator-lab/navigator/graph_schema.json`.
- The schema is experimental and may reflect old Skunkworks assumptions.
- It may not fully match the broader object families proposed in `COSMOS_SCHEMA_NOTES.md`.
- It is not canonical truth.
- This review should not create the real `cosmos/schemas/` directory yet.

## 9. Recommendation

Safe to copy later after operator approval and a boundary note, if this review is accepted.

Do not copy it now.

## 10. Required Label If Copied Later

“This schema is a derived Zibaldone/Skunkworks archaeology artifact and early AXIS-Cosmos/Navigator graph contract candidate. It is not Canon and remains experimental until accepted by the Cosmos schema process.”

## 11. Next Safe Step

Create the next review note for `cosmos_graph.json`, because it is a small fixture candidate and can test the schema shape after `graph_schema.json` review.

Do not create it in this pass.

## 12. Do Not Touch Confirmation

- Files created/modified: created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/fixture-reviews/graph_schema_REVIEW.md`; modified `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/fixture-reviews/README.md`.
- Production touched: no.
- Published touched: no.
- Candidate copied: no.
- Zibaldone files copied: no.
- Schemas, code folders, or scripts created: no.
- Git initialized: no.
- Builds, pipelines, scripts, or provider calls ran: no.
- Commits, pushes, or deploys happened: no.
