# Phase 1 — remaining guided review

Current progress: round 10 completed; two planned short business-decision rounds remain (11 and 12), followed by one consolidated requirements review. Original planning estimate after round 9 was three remaining rounds. Additional questioning should be limited to material new blockers, not routine implementation details. This plan is an estimate, not an owner-approved requirement or fixed deadline.

## Covered in rounds 1–9

Production replacement scope and pilot; ordinary/entity/application-wide roles; Business Owner reporting and transfer approvals; respondent participation/history; scoped exports and reminders; privileged role administration; reopening/reassignment; historical preservation; bulk validation/create-only imports; sale/non-sale disposal; lightweight quantity-inventory transfers. Source: D001–D032 in ../decisions/DECISIONS.md.

## Remaining focused rounds

| Round | Focus | Decisions to consolidate |
|---|---|---|
| 10 — complete | Stock verification | D033–D035 confirm access-matrix/session scope, Available/In Use filtering, configurable default due date, discrepancy review and Business Owner sign-off with visible unresolved exceptions. |
| 11 | Accounting reconciliation | Ledger comparison/discrepancy treatment, explicit review/approval ownership and whether/how accepted results change operational data. Preserve baseline matching rules as evidence for review. |
| 12 | Acceptance and rollout constraints | Success measures, priority user/device needs, business acceptance/support owners, any deadline and rollout constraints. Use returned company inventory for technical facts rather than asking the owner to guess. |

## Reduce interview overhead

Use engineering judgment for routine implementation details (naming, retries, concurrency protection, component behavior) within approved requirements; record consequential architectural choices for review. Carry baseline business rules forward as traceable draft assumptions when not superseded, clearly labeled rather than asserted approved. Ask the owner when a choice changes scope, authority, business outcomes or operating policy.

## Consolidated review outputs

One requirements summary, process maps, role/action matrix, acceptance criteria and prioritized implementation backlog. Identify unresolved company facts and remaining assumptions. The owner reviews this package together rather than being asked to approve each field separately.

## Technical evidence dependency

The read-only company environment inventory remains a separate source of facts. Closing business questioning does not establish deployment readiness or prove licenses, list schemas, backend permissions or app runtime behavior. Move architecture decisions forward where evidence is sufficient; keep evidence-dependent decisions explicitly pending.
