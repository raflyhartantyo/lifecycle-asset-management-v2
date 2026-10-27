# Stock_Opname_In_Use_Trigger — individual test plan

Read `../../Others/testing/SOLO-UAT-RUNBOOK.md` and this folder's IMPLEMENTATION.md, TRIGGER-CONTRACT.json, CONFIGURATION.json, ACTION-MAP.md and VALIDATION.md.

- Baseline characterization case: **FLOW-15** in `../../Others/testing/TEST-CASES.csv`.
- Related target V2 acceptance cases: SO-01, SO-03.
- Declared trigger fields: text; copy full types/required schema from TRIGGER-CONTRACT.json.

## Execute individually

1. Record the exact app/flow commit and development deployment version; bind controlled test connections and recipients.
2. Use synthetic employees/PIC metadata and assigned asset JSON with test notification sinks.
3. Source-defined grouped receiver/PIC notifications/status updates match fixture; campaign text/recipients reviewed before invocation.
4. Capture the run ID, response shape, touched action outputs and affected IDs. Exercise a safe malformed input/connector failure using the source's declared error path, and record gaps rather than assuming a handler.
5. Complete RESULT-LOG.csv with PASS/FAIL/BLOCKED/NOT RUN and cleanup. Characterization of a baseline flow is not a pass for target V2 changes it does not implement.

If the target feature depends on missing schema, connections, test identities or a rebuilt flow, mark that case BLOCKED. This document creates no deployment, enables no flow and authorizes no live recipients.
