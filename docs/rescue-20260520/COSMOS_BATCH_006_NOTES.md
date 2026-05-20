# COSMOS Batch 006 Notes

## Purpose

Batch 006 adds fixture inventory/index output only, with no semantic graph interpretation and no fixture mutation.

## Command Run

`python3 /home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py --root /home/sanghop/axis/axis-cosmos-lab --report /home/sanghop/axis/axis-cosmos-lab/outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md --inventory`

- Exit code: `0`

## Status

- PASS: `6`
- WARN: `2`
- FAIL: `0`

WARNs remain non-blocking SQL-derived archaeology context for:
- `fixtures/zibaldone/Grafo_Metricas.csv`
- `fixtures/zibaldone/Grafo_Conexoes_PDPN.csv`

## Inventory Output

- Generated: `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`
- Added fields:
  - relative path
  - artifact kind
  - present/missing
  - size
  - parse status
  - shallow consistency status
  - provenance class
  - canonical status
  - allowed future use

## Safety Confirmation

- Copied fixtures/artifacts modified: no.
- `Grafo_Conexoes_Report.md` edited: no.
- Production touched: no.
- Published touched: no.
- Git initialized: no.
- Builds/pipelines/provider/API/LLM/network calls: no.
