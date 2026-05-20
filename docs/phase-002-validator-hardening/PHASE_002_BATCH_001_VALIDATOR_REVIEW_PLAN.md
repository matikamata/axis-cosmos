# COSMOS Phase 002 Batch 001 Validator Review Plan

## 1. Purpose

This is a docs-only review plan before any validator/analyzer hardening.

## 2. Current State

- Rescue is closed (001–011b).
- Lab remains local-only.
- Lab is not a git repo.
- 6 copied seeds exist.
- Validator script exists.
- Analyzer script exists.
- Validation/analysis/inventory outputs exist.
- Production/published remain untouched by this flow.

## 3. Review Inputs

- `docs/phase-002-validator-hardening/PHASE_002_KICKOFF.md`
- `docs/rescue-20260520/COSMOS_RESCUE_20260520_CLOSURE.md`
- `docs/rescue-20260520/VALIDATION_SPEC.md`
- `docs/rescue-20260520/VALIDATOR_DESIGN.md`
- `outputs/validation/COPY_BATCH_001_VALIDATION_REPORT.md`
- `outputs/analysis/COPY_BATCH_001_ANALYSIS_REPORT.md`
- `outputs/analysis/COPY_BATCH_001_FIXTURE_INVENTORY.md`
- `scripts/validate_fixtures_readonly.py`
- `scripts/analyze_fixtures_readonly.py`

## 4. Validator Review

| Area | Current behavior | Limitation | Proposed hardening | Priority | Files likely affected |
|---|---|---|---|---|---|
| Path safety | strict root/protected-path checks | `--report` path is not safety-checked inside `run()` (only in `main`) | centralize safety checks in `run()` too, for defense-in-depth | MUST_FIX | `scripts/validate_fixtures_readonly.py` |
| Forbidden-pattern scan | credentials/local-path/SQL patterns scanned | pattern matching is broad and yields noisy context warnings | split “security fail” vs “context warn” pattern groups with explicit rationale tags | SHOULD_FIX | `scripts/validate_fixtures_readonly.py` |
| PASS/WARN/FAIL/BLOCKED accounting | per-file status and summary counts | mixed warnings in provenance inflate WARN count without prioritization | add warning classes (`context`, `format`, `safety`) in report | SHOULD_FIX | `scripts/validate_fixtures_readonly.py`, outputs report |
| JSON checks | parse + top-level keys + basic shape | no schema version compatibility warning path | add schema-version mismatch warning path (not fail by default) | NICE_TO_HAVE | `scripts/validate_fixtures_readonly.py` |
| CSV checks | delimiter/header/row required checks + numeric parse | no row-level sample context on failures | include first N failing row indexes for fast operator triage | SHOULD_FIX | `scripts/validate_fixtures_readonly.py` |
| Markdown/provenance checks | non-empty + derived wording scan + markers | provenance markers rely on exact phrasing, causing avoidable warnings | accept marker aliases / normalized token checks | MUST_FIX | `scripts/validate_fixtures_readonly.py` |
| Graph consistency checks | concept edge-source/target linkage checks | no explicit severity policy threshold | add threshold policy (e.g., >X unresolved edges => FAIL, else WARN) | SHOULD_FIX | `scripts/validate_fixtures_readonly.py` |
| Report readability | comprehensive narrative report | long output makes triage slower | add compact “Top issues” section with ordered severity | SHOULD_FIX | `scripts/validate_fixtures_readonly.py`, outputs report |
| Operator dashboard usefulness | high-level status doc | not auto-linked to validation deltas | add optional report snippet block (manual docs step, not automation) | DEFER | docs-only later |

## 5. Analyzer Review

| Area | Current behavior | Limitation | Proposed hardening | Priority | Files likely affected |
|---|---|---|---|---|---|
| Path safety | strict root/report path safety | inventory path is fixed; not configurable | optional explicit `--inventory-path` with same safety constraints | NICE_TO_HAVE | `scripts/analyze_fixtures_readonly.py` |
| PASS/WARN/FAIL accounting | FAIL if any file FAIL, WARN for SQL-derived CSVs | no separate counter for context-only WARN classes | add warn subtype tags in report and summary | SHOULD_FIX | `scripts/analyze_fixtures_readonly.py`, outputs report |
| JSON checks | parse/type/keys/non-empty checks | no optional strict mode | add `--strict-shape` mode (off by default) | DEFER | `scripts/analyze_fixtures_readonly.py` |
| CSV checks | delimiter/header/row checks via sniff | sniffer may be brittle on edge files | fallback deterministic delimiter policy if sniff fails | MUST_FIX | `scripts/analyze_fixtures_readonly.py` |
| Markdown/provenance checks | derived wording detection | wording detection is heuristic only | add explicit phrase set + fallback heuristic | SHOULD_FIX | `scripts/analyze_fixtures_readonly.py` |
| Graph consistency checks | shallow consistency only | no cross-file consistency between graph/paths/schema | add optional shallow cross-check block (non-semantic) | NICE_TO_HAVE | `scripts/analyze_fixtures_readonly.py` |
| Report readability | table + consistency + findings | no concise operator delta since last run | add “run delta” placeholder section (manual or optional) | DEFER | analyzer + docs process |

## 6. Report / Operator UX Review

| Report or doc | Current usefulness | Limitation | Proposed improvement | Priority |
|---|---|---|---|---|
| `COPY_BATCH_001_VALIDATION_REPORT.md` | deep validator detail | some warnings are formatting-noise-heavy | add grouped warning classes + top 5 actions | MUST_FIX |
| `COPY_BATCH_001_ANALYSIS_REPORT.md` | clear per-file shape summary | limited distinction between risk and context | split “risk warnings” vs “context warnings” | SHOULD_FIX |
| `COPY_BATCH_001_FIXTURE_INVENTORY.md` | strong index and boundaries | no “review freshness” marker | add generated-at + review-window hint | NICE_TO_HAVE |
| `COSMOS_OPERATOR_DASHBOARD.md` | good overview | manual sync burden | add explicit pointer to latest validation/analysis timestamps | DEFER |

## 7. Minimal Hardening Scope Recommendation

Smallest safe `COSMOS_PHASE_002_BATCH_002_VALIDATOR_MINIMAL_HARDENING` scope (only after explicit approval):

- adjust `scripts/validate_fixtures_readonly.py` for:
  - provenance marker normalization (MUST_FIX),
  - warning class separation (SHOULD_FIX),
  - top issues summary block (SHOULD_FIX).
- adjust `scripts/analyze_fixtures_readonly.py` for:
  - CSV delimiter fallback safety (MUST_FIX),
  - warning class separation (SHOULD_FIX).
- regenerate explicit reports only under `outputs/validation/` and `outputs/analysis/`.
- add one Phase 002 batch report doc.

Allowed candidate files for future Batch 002 only:
- `/home/sanghop/axis/axis-cosmos-lab/scripts/validate_fixtures_readonly.py`
- `/home/sanghop/axis/axis-cosmos-lab/scripts/analyze_fixtures_readonly.py`
- explicit new reports under `/home/sanghop/axis/axis-cosmos-lab/outputs/`
- one Phase 002 batch report doc

No fixture mutation.

## 8. Forbidden For Batch 002

- no production/published changes;
- no fixture edits;
- no copied seed edits;
- no new Zibaldone files;
- no old script execution;
- no git/deploy;
- no provider/API/LLM/network;
- no schema redesign;
- no renderer/UI work.

## 9. Approval Gates Before Batch 002

- operator approval required;
- file scope must be explicit;
- outputs path must be explicit;
- scripts may only be local/read-only;
- fixtures must not mutate.

## 10. Recommended Next Step

Operator reviews this plan and explicitly approves or edits the Batch 002 scope.

## 11. Do Not Touch Confirmation

- File created: `/home/sanghop/axis/axis-cosmos-lab/docs/phase-002-validator-hardening/PHASE_002_BATCH_001_VALIDATOR_REVIEW_PLAN.md`
- Files modified: none.
- Production touched: no.
- Published touched: no.
- Fixtures/artifacts/scripts/outputs modified: no.
- Existing scripts executed: no.
- Git initialized: no.
- Builds/pipelines/provider/API/LLM/network calls ran: no.
- Commits/pushes/deploys happened: no.
