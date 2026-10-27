# Individual UAT kit

The project owner is the sole human tester. The main developer supplies cases and fixes; company Claude assists authorized setup/implementation. There are **78 cases**: 63 target V2 acceptance cases and 15 individual baseline-flow characterization cases. All are initially NOT RUN. No app/flow was deployed or runtime-tested by preparing this kit.

## Start

1. Read [SOLO-UAT-RUNBOOK](SOLO-UAT-RUNBOOK.md).
2. Complete [SETUP-CHECKLIST](SETUP-CHECKLIST.md) and [PERSONA-BINDINGS](PERSONA-BINDINGS.csv).
3. Map/seed [synthetic fixtures](fixtures/README.md) only in development/test.
4. Run [TEST-CASES](TEST-CASES.csv) in sessions; record [RESULT-LOG](RESULT-LOG.csv) and [DEFECT-LOG](DEFECT-LOG.csv).
5. Follow [UNIT-TEST-MAP](UNIT-TEST-MAP.md) for one app/flow at a time.

Use a company-side copy for actual results/identities/evidence. Keep repository templates reusable and avoid committing credentials, live business rows or unredacted payloads. Test cases validate target behavior only after the corresponding rebuilt component is delivered; baseline characterization has a separate basis label.

## Status rules

PASS: observed expected result for the selected version, with evidence. FAIL: observed mismatch. BLOCKED: missing prerequisite or unresolved contract prevents execution. NOT RUN: not attempted. Missing test accounts/permissions/fixtures are never counted as a security pass. Emulation evidence and actual company-device evidence are recorded separately.

Critical: cross-scope leakage/unauthorized privileged change, history/asset loss or equivalent severe integrity failure. High: retained core workflow blocked or incorrect material results without a safe workaround. Medium/Low: triage by business impact. No unresolved Critical/High defect may pass the confirmed release gate; required blocked tests keep that gate unproven.

Local kit consistency can be checked from repository root with `python3 Others/tools/validate_uat_kit.py`; this checks template/fixture structure and traceability, not runtime behavior.
