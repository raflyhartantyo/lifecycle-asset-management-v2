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


## D011 — Business Owner meaning

Phase 1 round 3: Business Owner means the person accountable for particular assets, represented by the existing asset Business Owner field. Asset Manager handles operational management. Approval authority is assigned explicitly rather than being automatically inherited from asset ownership.

## D012 — Respondent as task participation with history

Phase 1 round 3: Respondent is request-specific participation, not a permanent broad application role. Participants may access processes historically assigned to them, including completed processes, in read-only form. Responses are editable only during the participant's open response step; explicit audited reopening is required for later edits. This extends D010's edit restriction with historical read access. Exact historical detail visibility and offboarding/access-revocation rules remain to be specified.

## D013 — Entity and global administration scopes

Phase 1 round 3: introduce Global User for maintenance throughout one assigned entity, across that entity's functions. Super User is the developer-like administrative role for maintenance across all entities and functions. These are explicit administrative exceptions to D002/D007's ordinary email/entity/function access boundaries. Ordinary business roles remain pair-scoped. The canonical role spelling is Super User (formerly Superuser); there are seven permanent role names including Global User, with Respondent modeled separately as task participation.

The owner confirmed maintenance scopes. Detailed permissions for granting privileged roles, business approval steps, destructive changes and developer operations still require an action matrix. Application role assignments do not themselves provision company-side maker/environment permissions; deployment access must be configured in the company environment. Every operational record retains its valid entity/function pair even when maintained by a broader administrator.


## D014 — Business Owner reporting oversight

Phase 1 round 3 follow-up: owner explicitly requested Business Owner access to the reporting side, including checking request progress. Business Owners can monitor the progress/status of relevant processes in their authorized business scope. Detailed reporting visibility, exports, follow-up/reminder actions and report-definition editing are still to be specified; progress monitoring does not silently grant these additional write/administration permissions.


## D015 — Asset Operator and Asset Manager duties

Phase 1 round 4: Asset Operator registers and moves assets in authorized scope. Asset Manager additionally runs stock verification, accounting reconciliation and direct disposal in authorized scope. Asset Operator alone does not grant direct disposal. Self-approval remains governed by D009 and explicit workflow-step authority.

## D016 — Business Owner process visibility

Phase 1 round 4: Business Owner reporting includes requests involving their business-owned assets even when initiated by another person. Expose relevant progress and asset details within authorized business scope. Export, follow-up actions and report editing remain separate permissions; ownership/report visibility does not expose unrelated records in a mixed-owner request.

## D017 — Privileged role administration

Phase 1 round 4: Global User may maintain ordinary business-role assignments within its assigned entity. Only Super User may grant/revoke Global User and Super User privileges. Grant scope must stay within the administrator's authority; ordinary role combinations must not indirectly confer privileged role administration.


## D018 — Viewer and Inventory Operator basics

Phase 1 round 5: Viewer has read-only access to authorized records/reports. Inventory Operator registers quantity inventory, transfers quantities and views inventory history within its assigned organization/function. Export is a permitted read operation under D019, not a business-data edit.

## D019 — Assigned-data and scoped exports

Phase 1 round 5: owner amended the proposed export restriction: Viewer and Respondent can export data assigned to them. Viewer exports stay within assigned data and authorized scope. Respondent exports stay within their assigned process/data visibility, including readable historical assigned work; no unrelated records/fields are exposed. Preserve the other proposed export scopes: Asset/Inventory Operator exports its authorized module data; Asset Manager exports in-scope operational data; Business Owner exports relevant owned-asset reports; Global User exports within its entity; Super User exports across entities. Export filters and field visibility match authorized access; formats, field lists and historical detail boundaries remain to be specified.

## D020 — Reminder authority

Phase 1 round 5: both Business Owner and Asset Manager can send standard reminders to pending respondents on relevant requests within their authority. Reminders do not themselves edit responses, complete a process or reopen closed work. Recipient selection, rate limiting, delivery and audit details are designed later.


## D021 — Audited reopening

Phase 1 round 6: Asset Manager, Global User and Super User may reopen closed processes within their respective scope, with a required reason and audit record. Business Owner may request reopening but does not execute it through that role alone. Preserve prior responses and decisions. Workflow-specific reset/reapproval rules are still to be defined.

## D022 — Respondent task reassignment

Phase 1 round 6: Asset Manager, Global User and Super User may reassign respondent tasks within their authority. Record the reason, audit the change and notify affected participants. Former respondents retain read-only history of their assigned work; replacement respondents receive explicit task access. This decision does not define final-approver reassignment/delegation rules, which remain a workflow-design question.

## D023 — Historical preservation and routine record removal

Phase 1 round 6: normal application actions archive, retire or cancel records with retained history rather than permanently deleting historical/audit evidence. Permanent removal of historical/audit records is a separately controlled maintenance operation governed by company retention requirements. No retention duration is assumed. Direct disposal removes the asset from the active register while preserving disposal/history records.


## D024 — Bulk registration with valid-row confirmation

Phase 1 round 7: validate the spreadsheet first and preview valid/invalid rows. The operator may confirm importing only valid rows; invalid rows remain unimported with a downloadable error report. Preserve row-level outcomes. Detailed mandatory fields, duplicate rules, retry safety and partial-write recovery remain to be designed and verified.

## D025 — Cross-function/entity transfer approvals

Phase 1 round 7: support transfers between functions and entities with approval from both the outgoing and receiving Business Owners. Preserve asset identity and traceable history and validate source/destination authority. The confirmed business approval requirement means the transfer is applied only after both required approvals; request status and final transfer completion are separate. Scope transfer does not grant unrelated destination-data access. Approval routing order, same-person handling, rejection/resubmission and within-scope Business Owner changes remain to be settled.

## D026 — BAU asset transactions have no mandatory remarks/reason

Phase 1 round 7: routine asset transactions are business-as-usual and require no remarks or reason entry. Do not introduce an extra mandatory justification step for ordinary asset registration/movement/status/ownership transactions. Capture actor, time and previous/new values automatically for history. This supersedes the proposed mandatory movement-reason requirement. D021/D022's required reasons for exceptional reopening and respondent reassignment remain unchanged.


## D027 — Same-person transfer approval

Phase 1 round 8: if the outgoing and receiving Business Owner are the same person, one explicit approval satisfies both capacities. Record both capacities and the decision; no silent automatic approval is introduced. D009's absence of a blanket self-approval ban remains applicable.

## D028 — Rejected transfers and corrected resubmission

Phase 1 round 8: rejection by either required Business Owner ends the transfer request as rejected and leaves the asset unchanged. A corrected request may be submitted while preserving the previous request's history. Exact status labels and pending sibling-approval cleanup are implementation design details.

## D029 — Business Owner changes within a scope

Phase 1 round 8: changing Business Owner requires outgoing and receiving Business Owner approval even when organization/function stay the same. Location, asset-custodian or status changes that leave organization, function and Business Owner unchanged remain BAU under ordinary permissions. Preserve asset identity/history and D026's absence of mandatory BAU remarks/reasons.
