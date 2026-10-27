# App individual test plan

Read `../../Others/testing/SOLO-UAT-RUNBOOK.md`, `IMPLEMENTATION.md`, `SCREEN-INDEX.md` and `VALIDATION.md`.

Use target cases in `../../Others/testing/TEST-CASES.csv`: AUTH identity/scope, REG registration/import, MOV movement/owner approval, DIS direct disposal, INV quantity inventory, SO physical verification, REC reconciliation, RPT reporting/export, UX devices/brand/accessibility and OPS recovery/rollback. Each case names its persona, exact fixture, steps, expected outcome, evidence and cleanup. Record in RESULT-LOG.csv and raise failures in DEFECT-LOG.csv.

Prepare one rebuilt feature and its dependency flows at a time. A valid original YAML file is not a runtime pass for new V2 requirements. Run screen-level App Checker/navigation checks from SCREEN-INDEX.md alongside feature cases; missing connections/media/components/permission enforcement remain blockers. Every rebuilt screen is assigned to the relevant business suite in its feature delivery.

One operator can test with several approved identities in isolated sessions. An administrator's UI role toggle does not validate restricted-user backend access. Do not run messages, approvals, mutations or failure injection against production.
