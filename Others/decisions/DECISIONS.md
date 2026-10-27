# Confirmed project decisions

## D001 — Disposal scope

Owner confirmation, 2026-10-27: keep direct asset disposal; retire only the separate disposal-request/approval process. Accounting reconciliation and stock-opname approvals remain in scope. Retained legacy files document the baseline and are not evidence that the target process remains approved.

## D002 — Entity and function hierarchy

Approved supplied redesign: Organization → Function → assets. A function belongs to one organization. Select gblEntity and gblFunction once per session. Reads/submissions and roles are scoped to that pair. One Roles row per (email, entity, function); multiple functions per user are allowed. CRESS starts empty. Backend isolation mechanism and final physical column contracts remain open.

## D003 — Delivery workflow

Owner confirmation, 2026-10-27: private GitHub repository in an approved account/organization, exactly three main folders (Power Apps, Power Automate, Others), one folder per app/flow, versioned complete replacement files, ready-to-paste Claude handovers, dependencies, implementation steps, validation and rollback.

## D004 — Baseline first

First delivery preserves the supplied implementation as reference and documents V2 scope and implementation order. Subsequent deliveries supply redesigned features. The main developer designs and prepares files; company Claude helps implement and returns exact outcomes/errors. Neither role implies a change to company authorization policies.


## D005 — First production replacement scope

Phase 1 round 1, owner confirmed: the first production replacement covers all retained capabilities (assets, quantity inventory, direct disposal, stock verification, accounting reconciliation, relevant approvals, audit/history, exports and reporting). Develop and test incrementally; separate disposal-request/approval remains excluded. Detailed acceptance criteria remain to be defined.

## D006 — Staged rollout

Phase 1 round 1, owner confirmed: pilot the completed candidate with ORG-01 / IT first; activate CRESS and further entities after configuration and acceptance. Validate IT/CRESS isolation before production acceptance even when CRESS has no operational assets.

## D007 — Explicit cross-entity assignments

Phase 1 round 1, owner confirmed: users may have explicit assignments across multiple organization/function pairs. Show only authorized pairs, select one active pair per session and grant no implicit access across pairs. D002's one-row-per-(email, entity, function) contract still applies; permission representation is a Phase 2 design decision.


## D008 — Owner-selected role names

Phase 1 round 2: use Viewer, Asset Operator, Inventory Operator, Asset Manager, Business Owner and Superuser. Respondent is tentative (owner wrote Respondent(?)); whether it is a permanent role or request-specific participation remains open. Detailed privileges and Superuser scope are not inferred from names. This replaces the previously proposed Stock Coordinator, Reconciliation Operator, Approver and Scoped Administrator role set; those responsibilities still need mapping.

## D009 — Self-approval policy

Phase 1 round 2: owner rejected a blanket rule preventing final approval of a request initiated by the same user. Self-approval is permitted when the user otherwise has explicit authority for the assigned approval step and scope. This does not give approval authority to all users or implicitly grant it to Superuser. Preserve initiator/approver identity and decision audit evidence. Direct disposal remains outside the retired separate disposal-request/approval process.

## D010 — Respondent boundaries

Phase 1 round 2: respondent permission covers only assigned requests/assets and allows response editing while the response step is open. Later corrections require an explicit audited reopening process. Broader access requires separate explicit permissions. This rule applies regardless of whether Respondent becomes a permanent role or request-level assignment.
