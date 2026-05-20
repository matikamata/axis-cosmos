# Cosmos Schema Notes

## 1. Purpose

This document plans the future AXIS-Cosmos graph schema before any fixture or code migration.

It converts the Zibaldone archaeology and source-map findings into a schema-contract direction only. No JSON schema file, fixture, code folder, or executable code is created in this pass.

## 2. Schema Role

The Cosmos schema should become the contract between:

- AXIS-NIDDHI canonical/static metadata;
- AXIS-Nana concept-map hints;
- AXIS-Navigator study/path data;
- AXIS-Cosmos analyzers/renderers;
- future Academy, sKullApp, and PitiPath consumers.

The schema should support both post-level graphs, such as PD#PN internal link relationships, and concept-level graphs, such as Navigator/Nana concept paths.

## 3. Canon-First Principle

- Cosmos schema is derived.
- Canon/CSL remains the source of truth.
- Cosmos graph objects are not canonical content.
- Every derived node and edge should carry provenance.
- Generated fixtures must be marked as derived.
- Cosmos must not mutate Canon, rewrite CSL, or become a hidden production build step.

## 4. Proposed Graph Object Families

Future schema families:

- `GraphBundle`
  - Container for one graph export, including nodes, edges, metrics, paths, provenance, and safety review.
- `Node`
  - A post, concept, section, cluster, path step, or other graph entity.
- `Edge`
  - A relationship between two nodes.
- `Metric`
  - Derived graph scores such as PageRank, degree, centrality, or hub score.
- `Cluster`
  - A derived constellation/grouping of related nodes.
- `Path`
  - A graph route or computed traversal.
- `StudyPath`
  - A curated learning sequence, likely shared with Navigator/Academy.
- `ConceptHint`
  - Nana-derived concept-map hint or graph hint.
- `Provenance`
  - Source, extraction method, generation policy, and derivation notes.
- `SafetyReview`
  - Sanitization and public-safety status for a bundle or fixture.

## 5. Proposed Node Fields

Possible node fields:

- `id`
- `kind`
- `label`
- `pdpn`
- `slug`
- `section`
- `language`
- `title`
- `group`
- `tags`
- `metrics`
- `provenance`
- `source_status`

Likely required later:

- `id`
- `kind`
- `label`
- `provenance`
- `source_status`

Likely optional later:

- `pdpn`
- `slug`
- `section`
- `language`
- `title`
- `group`
- `tags`
- `metrics`

Notes:

- Post nodes should usually carry `pdpn`.
- Concept nodes may not have a PD#PN and may instead use a stable `id` such as a concept slug.
- `kind` should distinguish `post`, `concept`, `section`, `cluster`, `path`, or other future node types.
- `source_status` should mark whether a node is `canonical_derived`, `sanitized_fixture`, `archaeology_only`, or `unreviewed`.

## 6. Proposed Edge Fields

Possible edge fields:

- `id`
- `source`
- `target`
- `relation_type`
- `weight`
- `evidence`
- `source_pdpn`
- `target_pdpn`
- `source_slug`
- `target_slug`
- `provenance`
- `extraction_method`
- `confidence`
- `review_status`

Possible `relation_type` values:

- `internal_link`
- `prerequisite`
- `study_path_next`
- `concept_related`
- `citation`
- `derived_similarity`

Notes:

- `source` and `target` should reference node IDs.
- `source_pdpn` and `target_pdpn` are useful for post-link graphs but should not be required for concept-only edges.
- `evidence` should point to safe derived evidence, not raw SQL.
- `extraction_method` should distinguish CSL/static-index extraction from SQL archaeology.
- `confidence` and `review_status` should make uncertain or legacy-derived edges explicit.

## 7. Metrics and Analysis

Planned derived metrics:

- PageRank;
- in-degree;
- out-degree;
- cluster id;
- centrality;
- hub score;
- orphan detection;
- unknown slug counts.

Metrics are derived and should be reproducible from sanitized inputs. Metric generation should be deterministic where possible, and metric bundles should record input fixture versions or source identifiers.

## 8. Provenance Requirements

Every bundle or artifact should record:

- source files used;
- extraction method;
- generation timestamp or deterministic build identifier policy;
- whether derived from SQL archaeology, CSL, static index, Navigator path data, or Nana concept hints;
- sanitization status;
- review status.

Provenance should make it impossible to confuse archaeology fixtures with canonical content.

## 9. Fixture Safety Requirements

Before any fixture enters the lab:

- size check;
- forbidden string/path scan;
- credential-like pattern scan;
- raw SQL exclusion;
- WordPress backup exclusion;
- source-vs-generated classification;
- public-safety decision.

Fixture review should decide whether the artifact is:

- safe to copy as-is;
- safe only as a trimmed sample;
- docs-only archaeology;
- forbidden/quarantined.

## 10. Compatibility Notes

Current Navigator graph schema:

- Uses `AXIS-COSMOS-GRAPH-V1`.
- Focuses on concept nodes with fields such as `concept_id`, `label`, `depth`, `citation_count`, `centrality_score`, `gravity_score`, `cluster_id`, `type`, and Pali display metadata.
- Defines relation types such as `depends_on`, `co_occurs`, `path_sequence`, `causal`, and `cessation`.

Zibaldone D3 constellation JSON:

- Appears post-level and PD#PN-oriented.
- Uses nodes/links suitable for D3 rendering.
- Includes section/group and PageRank-style metadata.

Future D3 renderer:

- Should consume a stable GraphBundle instead of ad hoc generated JSON.
- Should support small sanitized fixtures first.

Future Nana concept-map hints:

- Should feed ConceptHint and concept graph views.
- Should remain source-bound and not become free-form generated knowledge.

Future Academy study paths:

- May consume StudyPath and Path objects.
- Should distinguish curated paths from computed graph routes.

Cosmos should bridge both graph worlds: post-link topology and concept/study topology.

## 11. Open Questions

- Should PD#PN be mandatory for every post node?
- How should non-post concept nodes be identified?
- Should language variants be separate nodes or node attributes?
- Should large D3 JSON be stored, sampled, or generated on demand?
- What is the stable `relation_type` vocabulary?
- How much should Cosmos overlap with Navigator path schema?
- Should `AXIS-COSMOS-GRAPH-V1` be retained or revised for post-level graphs?
- Should metrics live inline on nodes/edges or in a separate `Metric` family?
- What fixture size threshold requires trimming or exclusion?

## 12. Next Safe Step

Recommended next safe step: create `REMOTE_REPO_ALIGNMENT.md`.

Reason: before copying fixtures or drafting actual schema files, Cosmos should clarify boundaries with existing public/local repos: `axis-navigator`, `axis-nana`, `axis-cli`, `axis-mirror`, `axis-preservation`, and protected `axis-niddhi` surfaces. This reduces the chance that Cosmos absorbs material that belongs in another repo.

## 13. Do Not Touch Confirmation

Files created/modified:

- Created `/home/sanghop/axis/axis-cosmos-lab/docs/rescue-20260520/COSMOS_SCHEMA_NOTES.md`.

Protected paths:

- `/home/sanghop/axis/axis-niddhi-production`: not touched.
- `/home/sanghop/axis/axis-niddhi-published`: not touched.

Execution safety:

- No Zibaldone files were copied.
- No schemas were created.
- No fixtures were created.
- No code folders were created.
- No scripts were created.
- Git was not initialized.
- No builds were run.
- No pipelines were run.
- No scripts were executed.
- No provider/API/LLM calls were run.
- No commits were made.
- No pushes were made.
- No deploys were made.

