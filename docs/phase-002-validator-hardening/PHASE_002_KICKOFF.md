# COSMOS Phase 002 Validator Hardening Kickoff

## 1. Purpose

Phase 002 is proposed as a validator/analyzer hardening phase after Rescue 20260520 closure.

## 2. Starting State

- Rescue 001–011b is closed.
- Lab remains local-only.
- Lab is not a git repo.
- No public repo exists.
- No deploy target exists.
- 6 copied seeds exist.
- Validator and analyzer scripts exist.
- Validation/analysis/inventory outputs exist.
- Production/published remain untouched by this flow.

## 3. Phase 002 Goal

- strengthen read-only validator/analyzer reliability;
- improve summary reports;
- improve safety checks;
- improve operator usability;
- preserve local-only posture.

## 4. Explicit Approval Gates

Before any code/script change, require:

Gate A — Operator Approval
- Operator explicitly approves the specific hardening batch.

Gate B — Scope Boundaries
- Batch states exactly which files may be modified.

Gate C — No Production/Published
- Batch confirms production/published are protected.

Gate D — No Fixture Mutation
- Validator/analyzer hardening must not mutate fixtures.

Gate E — No Provider/API/LLM
- No provider calls, API calls, LLM calls, or network calls.

Gate F — No Git/Deploy
- No git init, no commit, no push, no deploy.

Gate G — Report Safety
- Outputs may be written only to explicit `outputs/` paths.

## 5. Allowed Future Work, After Approval

- improve `validate_fixtures_readonly.py`;
- improve `analyze_fixtures_readonly.py`;
- add clearer report summaries;
- add stricter path safety checks;
- add better PASS/WARN/FAIL/BLOCKED accounting;
- add controlled smoke commands.

## 6. Forbidden Phase 002 Work

- public repo creation;
- git initialization;
- deploy setup;
- production/published edits;
- new Zibaldone migration;
- renderer/UI work;
- schema redesign;
- raw SQL usage;
- old script execution;
- provider/API/LLM calls.

## 7. Suggested First Phase 002 Batch

`COSMOS_PHASE_002_BATCH_001_VALIDATOR_REVIEW_PLAN`

Scope:
- docs-only review of current validator/analyzer behavior;
- identify minimal hardening targets;
- no code changes yet.

## 8. Do Not Touch Confirmation

- File created: `/home/sanghop/axis/axis-cosmos-lab/docs/phase-002-validator-hardening/PHASE_002_KICKOFF.md`
- Files modified: none in this pass.
- Production touched: no.
- Published touched: no.
- Fixtures/artifacts/scripts/outputs modified: no.
- Existing scripts executed: no.
- Git initialized: no.
- Builds/pipelines/provider/API/LLM/network calls ran: no.
- Commits/pushes/deploys happened: no.
