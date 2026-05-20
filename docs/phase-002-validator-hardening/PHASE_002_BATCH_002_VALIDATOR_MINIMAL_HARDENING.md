# COSMOS Phase 002 Batch 002 Validator Minimal Hardening

## 1. Purpose

Implement only the approved MUST_FIX items from Phase 002 Batch 001 review, with no scope expansion.

## 2. Approved Scope

1. Validator provenance marker normalization to reduce false WARN noise from exact-string matching.
2. Analyzer deterministic CSV delimiter fallback when `csv.Sniffer` fails or is ambiguous.
3. Validator report-path safety defense-in-depth in core run flow and immediately before write.

## 3. Files Modified

- `/home/sanghop/axis/axis-cosmos-lab/scripts/validate_fixtures_readonly.py`
- `/home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py`

## 4. Files Created

- `/home/sanghop/axis/axis-cosmos-lab/outputs/validation/PHASE_002_BATCH_002_VALIDATION_REPORT.md`
- `/home/sanghop/axis/axis-cosmos-lab/outputs/analysis/PHASE_002_BATCH_002_ANALYSIS_REPORT.md`
- `/home/sanghop/axis/axis-cosmos-lab/outputs/analysis/PHASE_002_BATCH_002_FIXTURE_INVENTORY.md`
- `/home/sanghop/axis/axis-cosmos-lab/docs/phase-002-validator-hardening/PHASE_002_BATCH_002_VALIDATOR_MINIMAL_HARDENING.md`

## 5. Pre/Post Script Hashes

Pre-change:

- `a2bb940f3e0caf7872057978d8545bffccd16a30105f34a6898c1a8a8b774078`  `scripts/validate_fixtures_readonly.py`
- `e6cc873b09c1e16fd0e98963a59130866270ae92811e836607f9727fc7c7f2e5`  `scripts/analyze_fixtures_readonly.py`

Post-change:

- `bed31bdb656eab61c62b5dc0bef90e929c1156b369eaac145176c1107037f29b`  `scripts/validate_fixtures_readonly.py`
- `d3b92a7e92e0a7e4493aff11a3a639982c30534c10501a4c330711883a529b81`  `scripts/analyze_fixtures_readonly.py`

## 6. Exact Script Changes Made

Validator (`validate_fixtures_readonly.py`):

- Added normalized marker matching utilities (`normalize_text`, `contains_marker`).
- Updated Markdown derived/non-canonical detection to accept equivalent marker phrases without exact sentence dependency.
- Updated provenance marker checks to use normalized/variant matching instead of brittle exact-string checks.
- Added report-path safety checks inside `run()` (defense-in-depth).
- Added second report-path safety check immediately before report write in `main()`.

Analyzer (`analyze_fixtures_readonly.py`):

- Added deterministic CSV delimiter detection fallback order: `;`, `,`, tab.
- Added delimiter detection method reporting in CSV facts.
- Added `--inventory-path` argument for explicit inventory output path.
- Enforced safety checks on explicit inventory path when `--inventory` is used.

## 7. Commands Run

Pre-change hashes:

`sha256sum /home/sanghop/axis/axis-cosmos-lab/scripts/validate_fixtures_readonly.py /home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py`

Validator run:

`python3 /home/sanghop/axis/axis-cosmos-lab/scripts/validate_fixtures_readonly.py --root /home/sanghop/axis/axis-cosmos-lab --report /home/sanghop/axis/axis-cosmos-lab/outputs/validation/PHASE_002_BATCH_002_VALIDATION_REPORT.md`

Analyzer run:

`python3 /home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py --root /home/sanghop/axis/axis-cosmos-lab --report /home/sanghop/axis/axis-cosmos-lab/outputs/analysis/PHASE_002_BATCH_002_ANALYSIS_REPORT.md --inventory --inventory-path /home/sanghop/axis/axis-cosmos-lab/outputs/analysis/PHASE_002_BATCH_002_FIXTURE_INVENTORY.md`

Post-change hashes:

`sha256sum /home/sanghop/axis/axis-cosmos-lab/scripts/validate_fixtures_readonly.py /home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py`

## 8. Validation Result Summary

- PASS: 4
- WARN: 4
- FAIL: 0
- BLOCKED: 0
- Exit code: 0

## 9. Analysis Result Summary

- PASS: 6
- WARN: 2
- FAIL: 0
- Exit code: 0
- New analysis report created at explicit Phase 002 path.
- New inventory report created at explicit Phase 002 path.

## 10. MUST_FIX Resolution Summary

1. Provenance marker normalization: resolved.
2. Deterministic analyzer CSV delimiter fallback: resolved.
3. Validator report-path safety defense-in-depth: resolved.

## 11. Files Intentionally Not Touched

- `outputs/validation/COPY_BATCH_001_VALIDATION_REPORT.md`
- `outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md`
- `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`
- Copied fixtures under `fixtures/zibaldone/`
- `docs/rescue-20260520/Grafo_Conexoes_Report.md`
- Production/published repositories

## 12. Do-Not-Touch Confirmation

- Production touched: no.
- Published touched: no.
- Fixtures modified: no.
- Copied seed files modified: no.
- Old Batch 001 reports modified: no.
- Git initialized: no.
- Builds/pipelines/provider/API/LLM/network calls: no.
- Commits/pushes/deploys: no.
