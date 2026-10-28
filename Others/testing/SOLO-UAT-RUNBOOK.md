# Single-operator UAT runbook

You conduct all human tests yourself. Personas are the permission contexts you exercise, not additional human testers. Company Claude can guide setup within company access/tooling; the main developer provides versioned fixes and updated cases.

## First session: prepare without business execution

1. Read SETUP-CHECKLIST.md. Record the chosen development environment and current delivery commit.
2. Ask company Claude to complete ../handover/COMPANY-ENVIRONMENT-INVENTORY.md and identify which target components are actually deployed. Missing V2 features remain BLOCKED rather than being judged against an unchanged baseline.
3. Fill PERSONA-BINDINGS.csv with approved identity aliases and available grants. Arrange approved account provisioning through company administrators if needed; multiple identities can be controlled sequentially by one authorized test operator.
4. Map and seed fixtures per fixtures/README.md. Record actual IDs, counts, notification destinations and rollback references in company storage.
5. Run one harmless read under a restricted persona and confirm effective scope, then begin the case sequence.

## Suggested sessions

| Session | Cases | Focus |
|---|---|---|
| 1 | Setup, AUTH-01/02/03/07 | Identity and basic scope; stop unsafe side effects if authorization is broken |
| 2 | Remaining AUTH and REG | Privilege boundaries, registration, imports and duplicates |
| 3 | MOV | BAU movement and owner/scope approvals; use sequential distinct approved owner sessions |
| 4 | DIS and INV | Disposal preservation and lightweight quantity transfers; reset fixtures afterward |
| 5 | SO | Responding, discrepancies, history, reminders, sign-off, reopen and reassign |
| 6 | REC | Ledger comparison, explicit authorized correction application, then final task sign-offs on actual results (D070) |
| 7 | RPT and UX | Export/report scope, desktop/tablet/mobile and Zurich/accessibility |
| 8 | OPS and FLOW | Failure recovery, rollback and each selected baseline flow characterization |

Split sessions further as needed; this is an execution order, not a fixed completion-time estimate. Re-seed fresh affected fixtures between destructive/approval cases. Run security-negative cases using the real restrictive identity and backend enforcement, not an administrator impersonating a UI state.

## Execute a case

1. Read preconditions and requirement basis. Select exact version, persona, scope and fixture run.
2. Record before counts/values. Perform the listed steps without undocumented repair midway.
3. Compare actual with expected. Mark PASS/FAIL/BLOCKED/NOT RUN; attach a run ID or evidence reference and record cleanup.
4. On failure, write DEFECT-LOG with exact steps, control/action/source pointer if known, expected/actual values and impact. Preserve evidence; repeat only when useful for diagnosis or after a change.
5. Send a redacted result summary to the main developer: case IDs, version, expected/actual, error, run/evidence alias and defect severity. Apply the returned replacement via the company handover, retest the failed case and affected regression subset.

## Finish a candidate

Review all required cases for that candidate and map them to ACCEPTANCE-CRITERIA.md. Exclude reference-only characterization from the target-feature pass count. Required blocked/not-run cases are outstanding evidence. No unresolved Critical/High defect, authorization leakage or lost history can satisfy the gate. Record your observed acceptance assessment and remaining dependencies; company production-promotion authorization remains a separate company process.
