# Role and permission proposals — Phase 1 round 2

Status: proposed, awaiting owner response. Role names describe business responsibilities, not the physical Roles list schema. A user can hold several responsibilities within one email/entity/function assignment; this does not imply duplicate tuple rows.

## Proposed responsibility set

| Responsibility | Proposed purpose | Boundary needing detailed acceptance criteria |
|---|---|---|
| Viewer | Read authorized operational data and reporting | Export and reporting scope need explicit rules |
| Asset operator | Register and move individually tracked assets | Direct disposal is a separately granted permission, not automatically inherited |
| Inventory operator | Register and transfer quantity inventory | No automatic asset management rights |
| Stock coordinator | Start and manage physical stock verification | Final approval remains a separate authority |
| Reconciliation operator | Upload ledger data, run comparisons and prepare reconciliation | Final approval remains a separate authority |
| Respondent | Provide assigned physical-verification responses/evidence | Assigned open requests and assets only; no final approval implied |
| Approver | Make final decisions on assigned approval steps | No final approval of a request initiated by the same identity |
| Scoped administrator | Maintain authorized reference data and manage permitted access assignments | No automatic approval authority, cross-pair access or ability to exceed delegated administration scope |

## Proposed controls — not yet confirmed

1. Composable responsibilities scoped by organization/function, mapped into explicit permissions during architecture design.
2. Distinguish evidence/response confirmation from final approval. Block self-approval of requests initiated by the same user; administration does not create an exemption. The same person may hold operator and approver responsibilities for different requests.
3. Respondents see and change only their assigned requests/assets in the authorized pair while their response step is open. Changes after closure need an explicit reopening/reassignment process with audit, to be defined later.

## Follow-up after this round

Define who can dispose, edit accounting values, export data, maintain each reference list, assign roles, reopen requests or change assignments. Define named approval authorities, routing, delegation, escalation, substitutions and thresholds from company business owners. Decide reporting access separately, including Power BI permissions and scope enforcement. These details depend on the approved responsibility set and are not silently granted by this draft.
