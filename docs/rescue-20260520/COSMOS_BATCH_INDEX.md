# COSMOS Rescue Batch Index

This index summarizes the COSMOS rescue sequence as local rescue context only.

- Copied fixtures remain derived/non-canonical.
- Analyzer outputs remain derived/non-canonical.
- Inventory is an index only, not a graph.
- `Grafo_Conexoes_Report.md` remains archaeology/context only.
- CSL, identity records, lineage records, and future validated graph outputs remain authoritative.

| Batch | Title / Purpose | Status | Main artifact(s) | Code changed? | Fixtures changed? | Production/published touched? | Next-decision note |
|---|---|---|---|---|---|---|---|
| 001 | Docs + read-only validation checkpoint | Closed | `COPY_BATCH_001_REPORT.md`, `COPY_BATCH_001_PROVENANCE.md` | Yes (validator introduced later in flow continuity) | Yes (approved seed copy batch) | No | Continue with design-first validation path. |
| 002 | Analyzer skeleton design-only checkpoint | Closed | `COSMOS_ANALYZER_SKELETON_DESIGN.md`, `COSMOS_BATCH_002_CLOSURE.md` | No | No | No | Implementation deferred pending explicit approval. |
| 003 | First successful read-only analyzer skeleton checkpoint | Closed | `scripts/analyze_fixtures_readonly.py`, `outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md`, `COSMOS_BATCH_003_CLOSURE.md` | Yes | No | No | Keep analyzer minimal and read-only. |
| 004 | Shallow report enrichment checkpoint | Closed | enriched `COPY_BATCH_001_ANALYSIS_REPORT.md`, `COSMOS_BATCH_004_CLOSURE.md` | Yes (report-only enrichment logic) | No | No | Allow only shallow non-semantic report improvements. |
| 005 | Shallow consistency-check checkpoint | Closed | updated analyzer checks, `COSMOS_BATCH_005_CLOSURE.md` | Yes | No | No | Maintain PASS/WARN/FAIL separation with non-blocking provenance WARNs. |
| 006 | Fixture inventory/index checkpoint | Closed | `COPY_BATCH_001_FIXTURE_INVENTORY.md`, `COSMOS_BATCH_006_CLOSURE.md` | Yes (`--inventory`) | No | No | Use inventory as operator index only, not graph output. |
| 007 | Operator-facing inventory cross-reference checkpoint | Closed | `COSMOS_OPERATOR_DASHBOARD.md`, `COSMOS_BATCH_007_CLOSURE.md` | No | No | No | Strengthen operator guidance and authoritative-source boundaries. |
| 008 | Operator-facing rescue index/README checkpoint | Closed | `README.md`, `COSMOS_BATCH_008_CLOSURE.md` | No | No | No | Add global navigation for future operators. |
| 009 | Read-only batch index/table checkpoint | Closed | `COSMOS_BATCH_INDEX.md`, `README.md`, `COSMOS_BATCH_009_CLOSURE.md` | No | No | No | Consolidate rescue history before final handoff. |
| 010 | Final rescue handoff summary checkpoint | Closed | `COSMOS_RESCUE_HANDOFF_SUMMARY.md`, `README.md`, `COSMOS_BATCH_010_CLOSURE.md` | No | No | No | Pause/review sequence before any Batch 011. |
| 010b | Docs-only consistency sync | In progress | `README.md`, `COSMOS_BATCH_INDEX.md`, `COSMOS_OPERATOR_DASHBOARD.md`, `COSMOS_BATCH_010B_CONSISTENCY_SYNC.md` | No | No | No | Resolve timeline/wording drift; Batch 011 remains deferred. |

## Current Sequence Result

- Latest completed batch: 010
- Most recent analysis status: PASS 6, WARN 2, FAIL 0
- WARN meaning: non-blocking SQL-derived archaeology context for `Grafo_Metricas.csv` and `Grafo_Conexoes_PDPN.csv`

## Current Scope Marker

Batch 010b is a docs-only consistency sync. Batch 011 is not authorized in this pass.

Approval update: see `COSMOS_BATCH_010B_APPROVAL_CHECKPOINT.md` for accepted 010b sync and narrow Batch 011 authorization scope.
