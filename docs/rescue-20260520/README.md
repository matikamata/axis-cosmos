# AXIS-Cosmos Rescue 20260520

## 1. Purpose of This Rescue Folder

This folder is local rescue documentation/context for AXIS-Cosmos archaeology, fixture triage, safety policy, and staged operator decisions.

## 2. Current Safety Status

- Local-only workflow.
- Production/published paths are out of scope and untouched.
- No deploy surface.
- Copied fixtures are derived/non-canonical.
- Analyzer outputs are derived/non-canonical.
- Inventory is an index only, not a graph.

## 3. Batch Sequence Summary (001 to 010)

- Batch 001: docs + read-only validation checkpoint.
- Batch 002: analyzer skeleton design-only checkpoint.
- Batch 003: first minimal read-only analyzer skeleton run.
- Batch 004: shallow report enrichment checkpoint.
- Batch 005: shallow consistency-check checkpoint.
- Batch 006: fixture inventory/index checkpoint.
- Batch 007: operator-facing cross-reference checkpoint.
- Batch 008: operator-facing rescue index/README checkpoint.
- Batch 009: read-only batch index/table checkpoint.
- Batch 010: final rescue handoff summary checkpoint.

## 4. Key Files and What Each One Is For

- `COSMOS_RESCUE_HANDOFF_SUMMARY.md`: final operator-facing rescue handoff summary across Batches 001–010.
- `COSMOS_BATCH_INDEX.md`: read-only batch index/table for Batches 001–010.
- `COSMOS_OPERATOR_DASHBOARD.md`: concise operator status board.
- `COPY_BATCH_001_REPORT.md`: copy-batch execution and safety record.
- `COPY_BATCH_001_INTEGRATION_PLAN.md`: how copied seeds connect before code work.
- `VALIDATION_SPEC.md`: docs-only validation contract.
- `VALIDATOR_DESIGN.md`: implementation design for read-only validator.
- `FIXTURE_SANITIZATION_CHECKLIST.md`: required safety gates before copying fixtures.
- `FIXTURE_MANIFEST_DRAFT.md`: candidate fixture manifest and destination intent.
- `DERIVED_ARTIFACT_LABELS.md`: explicit labeling for non-canonical artifacts.
- `ZIBALDONE_COSMOS_SOURCE_MAP.md`: source-to-seed archaeology mapping.
- `SQL_EXTRACTION_ARCHAEOLOGY.md`: old SQL-dependent path documented as archaeology.

## 5. Derived / Non-Canonical Warning

All rescue fixtures and analyzer outputs in this workflow are derived/non-canonical context artifacts.  
`Grafo_Conexoes_Report.md` is archaeology/context only and must not be treated as authoritative graph truth.

CSL, identity records, lineage records, and future validated graph outputs remain authoritative.

## 6. Where to Find Analysis and Inventory Outputs

- Analysis report: `outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md`
- Fixture inventory index: `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`
- Copy provenance: `fixtures/zibaldone/COPY_BATCH_001_PROVENANCE.md`

## 7. What Not To Do

- Do not treat rescue artifacts as Canon.
- Do not execute old Zibaldone scripts.
- Do not copy raw SQL, WordPress backups, credentials, caches, or generated static trees.
- Do not run builds/pipelines/provider calls from this rescue lane.
- Do not add semantic graph claims, rankings, or merged graph outputs in rescue docs batches.

## 8. Next Safe Step

After explicit approval, use `COSMOS_BATCH_INDEX.md` as the starting point for any new rescue batch decision and add only read-only operator documentation updates.

For end-to-end rescue context handoff, start with `COSMOS_RESCUE_HANDOFF_SUMMARY.md`.

Batch 011 remains deferred until consistency-sync updates are reviewed.
