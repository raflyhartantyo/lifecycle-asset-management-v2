# Phase 1 — requirements and scope

Status: draft for guided owner review. Proposed items are not approved decisions.

## Purpose

Redesign Lifecycle Asset Management V2 as a simple, consistent, Zurich-branded application that supports multiple organizations and their functions. Existing source provides business-rule and data evidence; the current layout is not the target design.

## Confirmed constraints and scope

- Platform baseline: Canvas App, Power Automate, SharePoint and Power BI. Final environment/licensing and backend authorization decisions remain open.
- Hierarchy: Organization → Function → assets. Every function belongs to one organization.
- Session context: select entity then function once; use gblEntity and gblFunction consistently.
- Ordinary business roles use one row per (email, entity, function), allowing multiple assignments. Global User is entity-wide across functions; Super User is application-wide across entities/functions (D013). Physical storage of these broader grants is a Phase 2 design decision.
- Retain direct asset disposal. Retire only the separate disposal-request/approval process; other approvals remain in scope.
- Zurich Design System rules govern visual design and accessibility.
- Delivery uses a private GitHub repository with Power Apps, Power Automate and Others, complete files and per-unit implementation/validation/rollback handovers.
- Main developer prepares designs/files; company Claude assists company-side implementation and returns evidence. Business owners accept outcomes.

## Capability inventory — first production replacement

| ID | Capability | Established target scope |
|---|---|---|
| CAP-01 | Identity, roles and organization/function selection | Required foundation |
| CAP-02 | Master data and asset register | Retained |
| CAP-03 | Individual asset registration and movement | Retained |
| CAP-04 | Direct asset disposal | Retained by owner decision D001 |
| CAP-05 | Quantity inventory registration and transfers | Retained |
| CAP-06 | Available/in-use stock verification and relevant approvals | Retained |
| CAP-07 | Accounting reconciliation and relevant approvals | Retained |
| CAP-08 | Audit/history, exports and reporting refresh | Retained |
| CAP-09 | Separate disposal request/approval | Retired from target V2 |

## Round 1 — confirmed by owner

1. First production replacement covers all retained capabilities; develop them incrementally in the development environment rather than releasing a production replacement with essential current workflows missing.
2. Pilot the completed production candidate with ORG-01 / IT first. Validate IT/CRESS isolation before production acceptance; activate CRESS usage after its setup and acceptance. Add other entities through verified configuration and staged onboarding.
3. Permit users to have explicit role assignments across more than one organization/function pair. Show only authorized pairs, with an active session pair. A role in one pair grants no implicit access to another.

## Round 2 — owner responses recorded

- Owner-selected roles: Viewer, Asset Operator, Inventory Operator, Asset Manager, Business Owner and Superuser. Respondent remains tentative; duties, role combination and exact authority are pending.
- Owner rejected the blanket self-approval ban. A user may approve an initiated request when otherwise explicitly authorized for its assigned approval step/scope; permission is not created by this exception.
- Respondent access is limited to assigned open work; closing/reopening and audit rules apply. Additional responsibilities require their own explicit permission.

See D008–D010 and ROLE-PERMISSIONS-DRAFT.md. No permissions have been implemented.

## Round 3 — owner responses recorded

- Business Owner is the accountable owner identified on particular assets. Operational management belongs to Asset Manager; approval authority is explicit. Business Owner also has reporting oversight, including monitoring relevant request progress/status (D014).
- Respondent is task-specific participation. Users can read historical assigned processes, including closed ones; edit permissions remain limited to assigned open response steps.
- Global User maintains one assigned entity across all its functions. Super User maintains the whole application across entities/functions. These are explicit exceptions to ordinary pair-scoped access, not a change to record entity/function integrity.
- Permanent roles: Viewer, Asset Operator, Inventory Operator, Asset Manager, Business Owner, Global User and Super User. Exact action permissions and privileged-role assignment authority remain open.

## Round 4 — owner responses recorded

- D015: Asset Operator registers/moves assets. Asset Manager additionally runs stock verification and accounting reconciliation and performs direct disposal in scope. Operator role alone does not grant direct disposal.
- D016: Business Owner can report on requests involving owned assets, even when initiated by others. Visibility is limited to relevant progress/details in authorized scope.
- D017: Global User administers ordinary role assignments within its entity. Only Super User grants/revokes Global User and Super User privileges.

## Round 5 — owner responses recorded

- D018: Viewer has scoped read-only access; Inventory Operator registers/transfers quantity inventory and views history.
- D019: Viewer and Respondent can export data assigned to them. All other proposed module/ownership/entity/application export scopes remain, with rows/fields filtered to authorized visibility. Historical exports do not exceed historical read access.
- D020: both Business Owner and Asset Manager may send standard reminders for pending relevant response tasks. Reminders do not change response/status or reopen work.

## Round 6 — owner responses recorded

- D021: Asset Manager, Global User and Super User may reopen closed work in scope with a required reason/audit; Business Owner may request reopening. Preserve prior answers/decisions.
- D022: those same roles may reassign respondent tasks in scope with a reason, audit and notifications. Previous respondents retain read-only historical visibility; replacements receive explicit task access.
- D023: normal app actions archive/retire/cancel while preserving history. Permanent historical/audit deletion is separately controlled under company retention requirements. Direct disposal preserves an inactive/history record while removing the active record.

## Round 7 — owner responses recorded

- D024: validate and preview spreadsheet rows; import only valid rows the operator confirms. Invalid rows remain unimported with a downloadable error report.
- D025: cross-function/entity transfers require approval from both outgoing and receiving Business Owners, retaining identity/history and source/destination authorization.
- D026: no mandatory remarks/reason entry for BAU asset transactions. Record change history automatically. Existing exceptional reopening/reassignment reason requirements remain.

## Round 8 — owner responses recorded

- D027: the same person acting as both Business Owners gives one explicit approval, recorded in both capacities.
- D028: either owner's rejection ends the transfer request as rejected without changing the asset. Corrected requests preserve prior request history.
- D029: Business Owner changes require both approvals even within one entity/function. Location/custodian/status changes that change none of entity/function/Business Owner remain BAU under permissions.

## Round 9 — owner responses recorded

- D030: registration/import creates new assets only. Report identified duplicates without overwriting existing assets; existing-record changes use authorized edit/movement processes.
- D031: direct disposal supports sale and non-sale retirement. Require disposal date; buyer/price details apply to sales. No mandatory BAU remarks/reason.
- D032: inventory is managed more lightly than individually tracked assets. Inventory transfers do not require outgoing/receiving Business Owner approval. Retain scope/authority, quantity and history controls; do not add a Business Owner relationship solely for the rejected inventory approval proposal.

## Round 10 — stock verification owner responses recorded

- D033: derive entity/function from access matrix and active authorized session; filter assets by Available/In Use; include due date with a configurable default. Never infer unrestricted scope from a visible selection control.
- D034: respondents provide presence/condition/discrepancy evidence; Asset Manager reviews differences and authorized processes apply master-record corrections.
- D035: Business Owners sign off relevant results. A cycle may close with explicitly acknowledged unresolved exceptions, which remain visibly unverified.

## Round 11 — reconciliation owner responses recorded

- D036: comparison preview includes matches, missing records on either side, value/quantity differences and disposal exceptions; retain accounting period/file/run history.
- D037: configured Accounting and Governance approvers sign off in entity/function scope through explicit workflow assignments; no new permanent role names are required.
- D038: after sign-off, authorized Asset Manager explicitly reviews/applies proposed corrections with preview/audit. Uploading/comparing alone does not create/dispose assets or change ownership/scope; existing action approvals remain applicable.

## Round 12 — owner responses recorded

- D039: desktop/laptop primary; responsive tablet support; mobile-friendly responses, approvals and progress viewing.
- D040: acceptance gate confirmed; main developer supplies concrete test cases/setup/expected results, and company-side execution supplies evidence.
- D041: project owner is the sole human UAT tester. Provide sequential individual-testing sessions using approved identities/personas; company Claude can assist setup. Post-launch support ownership and fixed go-live date remain unspecified, not assumed.

## Guided interview status

All twelve planned business-decision rounds are complete. The consolidated review package is PHASE-1-REVIEW-PACKAGE.md, with process maps, permissions, acceptance criteria, assumptions/dependencies and a prioritized backlog. This is ready for owner review, not a claim of company runtime/deployment readiness or formal requirements sign-off. Routine engineering details are recorded as labeled assumptions; material company facts remain explicit dependencies.

## Company-side fact collection task

Give company Claude `../handover/COMPANY-ENVIRONMENT-INVENTORY.md`. This read-only inventory establishes environment, deployment, schema, permissions, scale and asset availability without waiting for every role decision. Technical conclusions are deferred until the returned facts are verified.

## Later decisions and evidence

- Post-launch support/promotion authority and company-specific operational ownership; UAT execution is assigned to the project owner (D041).
- Company-side evidence for acceptance targets, numerical performance benchmarks and any fixed go-live deadline; release capability scope is already confirmed.
- Process-specific permission/field/routing details in the assumptions register; the confirmed role/action matrix remains authoritative.
- Expected devices, user volumes, data growth, concurrent usage and performance targets.
- Detailed process rules, canonical statuses and lifecycle state transitions.
- Migration retention, historical data reconciliation and cutover expectations.
- SharePoint column contracts and backend authorization design.
- Target environment capabilities, licenses, DLP/connector restrictions, solution support and deployment permissions.

## Company-side fact collection

An independent read-only environment inventory can establish actual environments, available deployment tooling, existing app/flow versions and dependencies. SharePoint internal column metadata, existing permissions and list sizes should come from company systems. Report availability and constraints rather than credential values or personal data. Technical design choices follow that evidence; missing facts are not assumed to be negative answers.

## Phase completion

An agreed requirements document, capability/release scope, role/process matrix, measurable acceptance criteria, prioritized backlog and known constraints. Distinguish confirmed owner decisions, observed company-side facts and unresolved proposals. Record approved decisions in Others/decisions/DECISIONS.md with traceability to requirements and later acceptance tests.
