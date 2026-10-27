# Phase 1 — requirements and scope

Status: draft for guided owner review. Proposed items are not approved decisions.

## Purpose

Redesign Lifecycle Asset Management V2 as a simple, consistent, Zurich-branded application that supports multiple organizations and their functions. Existing source provides business-rule and data evidence; the current layout is not the target design.

## Confirmed constraints and scope

- Platform baseline: Canvas App, Power Automate, SharePoint and Power BI. Final environment/licensing and backend authorization decisions remain open.
- Hierarchy: Organization → Function → assets. Every function belongs to one organization.
- Session context: select entity then function once; use gblEntity and gblFunction consistently.
- Roles: one row per (email, entity, function), allowing multiple function assignments per user.
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

## Round 3 — proposed responsibility mapping awaiting owner response

1. Map retained stock-coordination and reconciliation responsibilities to Asset Manager; detailed direct-disposal, export and master-data permissions are still explicit decisions.
2. Define Business Owner as accountability for assigned assets/business area and authority only for designated approval tasks. Whether it is the same identity as the existing asset Business Owner field needs clarification before data design.
3. Keep Superuser administration within explicitly assigned organization/function pairs unless the owner approves a separate global administration exception.
4. Treat Respondent as request-specific participation rather than a permanent broad role, preserving D010 and explicit organization/function scope.

## Later decisions and evidence

- Business owner, operational users, approvers, support owner and acceptance authority.
- Measurable success criteria, MVP/release boundaries, priorities and any external deadline.
- Role/action matrix including read/edit/approve/export/admin rights and exceptional cases.
- Expected devices, user volumes, data growth, concurrent usage and performance targets.
- Detailed process rules, canonical statuses and lifecycle state transitions.
- Migration retention, historical data reconciliation and cutover expectations.
- SharePoint column contracts and backend authorization design.
- Target environment capabilities, licenses, DLP/connector restrictions, solution support and deployment permissions.

## Company-side fact collection

An independent read-only environment inventory can establish actual environments, available deployment tooling, existing app/flow versions and dependencies. SharePoint internal column metadata, existing permissions and list sizes should come from company systems. Report availability and constraints rather than credential values or personal data. Technical design choices follow that evidence; missing facts are not assumed to be negative answers.

## Phase completion

An agreed requirements document, capability/release scope, role/process matrix, measurable acceptance criteria, prioritized backlog and known constraints. Distinguish confirmed owner decisions, observed company-side facts and unresolved proposals. Record approved decisions in Others/decisions/DECISIONS.md with traceability to requirements and later acceptance tests.
