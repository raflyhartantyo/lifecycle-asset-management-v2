# Export Data — validation

Record target environment, flow version, app caller, test inputs and run ID.

1. Flow checker passes and trigger inputs match `TRIGGER-CONTRACT.json`, including file content/name shape and required fields.
2. All 9 indexed actions are present or their explicitly approved replacements are listed; every connector resolves in the target environment.
3. A representative valid request reaches the expected response and produces the expected list/file changes. Capture before/after values and counts.
4. Invalid/empty input and a simulated connector failure follow the source-defined error branch; record behavior when no explicit handler exists.
5. Every response action's output names and types match the bound Canvas caller. Test relevant conditions/approval outcomes using test recipients.
6. Verify writes, email/Teams delivery, approval records, generated links or dataset refresh only where this flow actually contains those operations. A placeholder/test-helper flow passes as reference-only and remains disabled.
7. Confirm current tenant/entity/function behavior as observed. V2 cross-function isolation remains pending a redesigned contract and backend enforcement; baseline behavior is not a V2 isolation pass.

Completion: return per-check PASS/FAIL/NOT RUN with run IDs, exact errors and cleanup/rollback outcome using `../../Others/handover/IMPLEMENTATION-RESULT-TEMPLATE.md`.
