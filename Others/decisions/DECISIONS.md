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


## D030 — Registration does not overwrite existing assets

Phase 1 round 9: registration/import creates new assets only. Identified duplicates are reported without overwriting existing records; existing-record changes use authorized edit/movement processes. Valid new rows can be imported under D024's preview/confirmation rules. Exact duplicate keys and retry outcome labels remain data-contract/design details.

## D031 — Sale and non-sale direct disposal

Phase 1 round 9: direct disposal supports sales and non-sale retirement. Disposal date is required; buyer/selling-price details apply to sales. No mandatory BAU remarks/justification field is added. Capture the appropriate inactive/history record and preserve D023's historical evidence.

## D032 — Lightweight quantity-inventory transfers

Phase 1 round 9: owner rejected applying asset-style dual Business Owner approvals to inventory because inventories are less tightly managed than assets. Inventory transfers use ordinary authorized inventory permissions, including supported cross-function/entity movements, without the dual Business Owner approval step. Preserve quantity validation, scope/authority checks and movement history; the absence of asset-style approval does not remove those controls. Do not add an inventory Business Owner relationship solely to implement the rejected approval proposal. Any other future inventory approval rule would require a separate explicit decision.


## D033 — Stock verification scope, filtering and due dates

Phase 1 round 10: derive entity/function from the access matrix and authorized session rather than free-form cycle selection. Filter the cycle's asset set by Available or In Use. Include a due date with a configurable default. For consistency with D002/D007/D013, a single authorized pair can be resolved automatically; multiple authorized pairs use the existing once-per-session authorized context selection, and broader administrators stay within their grant. This resolution detail is an engineering interpretation of the confirmed scope rules, not a new cross-scope permission.

Access matrix denotes the target authoritative permission source, not proof that the legacy Acces_Matrix already contains the required scope columns. Exact default duration, configuration ownership and physical permission schema are architecture/configuration details. Reviewable custodian/location-PIC respondent prefills remain a traceable baseline/design assumption for consolidated review.

## D034 — Stock verification discrepancies are evidence for review

Phase 1 round 10: respondents record asset presence, condition and ownership/location discrepancies. Differences go to Asset Manager for review. Responses are verification evidence; master-record changes use the authorized update process with history and applicable transfer approvals. A response does not silently rewrite ownership or scope.

## D035 — Stock verification sign-off and exception-aware completion

Phase 1 round 10: relevant Business Owners sign off their asset results. Every asset has either a verified outcome or an explicitly recorded unresolved exception. A cycle may close with acknowledged exceptions; unanswered or unresolved assets remain visibly unverified and never count as successfully verified. Preserve prior respondent/history/reminder/reopening rules. Exact states and exception implementation are specified during design.


## D036 — Reconciliation comparison preview and provenance

Phase 1 round 11: an uploaded accounting ledger produces a review of matched assets, records missing on either side, value/quantity differences and disposed-asset exceptions before register changes. Retain accounting period, source-file reference and reconciliation-run history. Exact matching/grouping and data-field definitions are validated against the baseline and company-side data contract during architecture/design.

## D037 — Accounting and Governance reconciliation sign-off

Phase 1 round 11: final reconciliation sign-off goes to configured Accounting and Governance approvers for the relevant entity/function through explicit workflow assignments. These responsibilities do not require additional permanent application roles. Assigned-task visibility and D009's absence of a blanket self-approval ban remain applicable. Configuration, routing order and substitutions remain design details for review.

## D038 — Explicit application of reconciliation corrections

Ordering update: D070 supersedes the original sign-off-before-application sequence below. Explicit authorization, preview, audit and action-specific prerequisites remain applicable.

Phase 1 round 11: after sign-off, an authorized Asset Manager explicitly reviews and applies proposed register corrections with a change preview and audit history. Upload/comparison alone does not automatically create/dispose assets or alter ownership/scope. Existing registration, disposal, transfer and field-edit authority requirements still apply. Approval and successful correction application are separate outcomes; preserve traceability of accepted versus actually applied changes.


## D039 — Supported device priorities

Phase 1 round 12: full operational/administration experience is primarily desktop/laptop, with responsive tablet support and mobile-friendly assigned responses, approvals and progress viewing. Validate exact supported browsers/device configurations in the company environment rather than claiming universal compatibility.

## D040 — Acceptance gate and developer-authored test cases

Phase 1 round 12: retained workflows must pass representative UAT, access isolation/audit/history/export permissions must be verified, Zurich brand/accessibility checks must pass and no unresolved critical/high defects remain. The main developer supplies the actual test cases, expected results, setup guidance and evidence/result templates. Company-side execution establishes outcomes; local artifact validation is not a runtime UAT pass.

## D041 — Sole human UAT tester

Phase 1 round 12: the project owner will personally conduct testing rather than assigning separate business-representative testers. Provide an individual-testing setup and staged runbook. Company Claude may assist permitted setup/implementation and the main developer supplies fixes/cases; neither substitutes for the owner's observed results. One test operator may use multiple company-approved test identities/personas sequentially. Unavailable independent identities/platform access leave the affected authorization/approval cases BLOCKED or NOT RUN; a UI role switch or one unrestricted account is not evidence that backend isolation passed. Post-launch support ownership and a fixed go-live date were not supplied and remain explicit dependencies.


## D042 — Microsoft Approvals for workflow decisions

Ordering update: D070 supersedes the reconciliation application-after-sign-off summary below. Transfer approvals still precede those transactions; final reconciliation sign-off follows actual application.

Owner direction, 2026-10-27: approvals will use Microsoft Approvals. Design the retained workflow decision steps around Microsoft approval services, with Power Automate orchestrating the LAM integration. This selects the approval platform; it does not introduce approvals into direct disposal or lightweight inventory transfers, change required approval capacities, or settle routing order, deadlines, delegation or reassignment policies.

Existing rules continue: outgoing and receiving Business Owner capacities for asset scope/owner changes; one explicit response when the same authorized person holds both capacities; rejection leaves the asset unchanged; stock result Business Owner sign-off; configured Accounting and Governance reconciliation sign-off; authorized explicit correction application afterward. LAM retains workflow progress, assigned-task context and historical evidence. Microsoft service access does not replace LAM scope authorization.

See `../architecture/MICROSOFT-APPROVALS-RESEARCH.md` for verified platform facts and `../architecture/APPROVALS-INTEGRATION-DESIGN.md` for the proposed integration and open implementation checks. No company approval flow was deployed or tested by this decision.


## D043 — Asset identifiers and accounting-code registration

Owner confirmations, 2026-10-27: LAM generates Asset Tags; their format/numbering scheme is explicitly deferred. The proposed LAM-000001 format is not approved. Accounting Asset Code is unique across the entire company and available at registration. Duplicate serial numbers are allowed. Accounting-code requiredness is a business validation rule for registration; do not permit duplicates or overwrite existing assets through registration. Exact canonicalization, case/whitespace handling, inactive-record reuse and safe tag allocation are forthcoming data-contract details, not settled here.

## D044 — Required fields controlled by the application

Owner confirmations, 2026-10-27: an Available asset can have no assigned custodian; In Use requires a custodian. Purchase date and purchase cost are mandatory business inputs. For all mandatory business fields, enforce requiredness through the Power Apps experience rather than SharePoint's Required column setting. Configure editable business columns as optional in SharePoint, including Title where configurable. Platform-managed fields and intrinsic storage types are not redefined by this preference.

This supersedes the Required=Yes settings in the first V2 foundation proposal. Keep business-required metadata separate from storage-required metadata. Uniqueness, types, indexes, access control and parent relationships remain separate integrity requirements. Applying the same business validations at flow/import mutation boundaries is an engineering recommendation to avoid alternate-entry inconsistency, not a new company approval policy. Direct SharePoint maintenance can produce incomplete rows; business operations must recognize them and guide correction rather than silently treat them as valid. Blank account codes do not satisfy registration even if storage permits them.

Lifecycle status labels/transitions remain under discussion. Available/In Use already distinguish stock-verification scope; this decision does not approve additional states or a maintenance module.


## D045 — Asset status, condition and approval progress

Owner agreed, 2026-10-27: use the label Asset Status for the asset's operational lifecycle, separate from physical Condition and request/approval progress. Available, In Use and Disposed were the agreed examples; final stored labels/transitions and condition choices will be finalized in the data contract. Available can have no custodian; In Use requires a custodian under D044. No maintenance module or additional status is approved by analogy.

## D046 — IDR and scheduled monthly Book Value calculation

Owner confirmed, 2026-10-27: currency is always IDR. Book Value will use a formula to be supplied later, applied by a scheduled flow at the start of every month. The uploaded accounting ledger is not selected as the automatic Book Value source. This replaces the proposed ledger-sourced Book Value design, not the retained reconciliation comparison/sign-off/explicit-correction process.

Formula, effective dates, asset eligibility, useful-life inputs if applicable, precision/rounding, minimum value, first/last-period handling, time zone/run time and correction/backfill rules are not yet defined. No formula or accounting convention is inferred. Monthly calculation needs its own auditable operation and reliable retry/recovery design; it must not conflate accounting sign-off with execution. No scheduled flow has been implemented, enabled or run. See `../architecture/MONTHLY-BOOK-VALUE-DESIGN.md` for the proposed engineering contract.


## D047 — Accounting-controlled asset categories

Owner confirmed, 2026-10-27: categories follow Accounting rules and are fixed as Komputer (KO), Non-Komputer (NK) and Perangkat Lunak (PL). These replace the illustrative IT/Furniture/Office category proposal. Accounting code definitions/mappings are deferred; KO/NK/PL are the supplied abbreviations, not an inferred full accounting-code scheme. Do not confuse category accounting mappings with the company-wide unique Accounting Asset Code assigned to each asset (D043).

## D048 — Asset Type parent lookup and software enhancement treatment

Owner confirmed, 2026-10-27: Asset Type has a foreign-key lookup to Category. Design each type as belonging to one category; business-requiredness is enforced through the application under D044 rather than SharePoint Required flags. The final lookup/list names and physical contracts will be delivered with reference-data setup.

Perangkat Lunak represents internal software enhancements budgeted/capitalized and documented as assets. Use the same registration fields as other assets; no separate licence/subscription module or software-specific registration form is requested. Exact type names, reference-data administration authority and category-change rules remain to be specified. See `../architecture/ASSET-CLASSIFICATION-DESIGN.md` for the distinction between confirmed requirements and proposed UI/integrity behavior.


## D049 — Shared locations across entities and functions

Owner confirmed, 2026-10-27: locations are reusable by multiple functions and multiple entities; most represent shared buildings. Use shared location reference records rather than making each location exclusively owned by an organization/function or duplicating the same building per entity. Asset organization/function remains the authority scope; a common location does not grant cross-scope asset, inventory, report or task access.

Location granularity (building alone versus building/floor/room), finer location relationships, site codes, deactivation rules and location-maintainer authority remain to be designed. Shared physical buildings do not automatically imply a shared custodian, Business Owner, respondent or approver. See `../architecture/LOCATION-DESIGN.md`.


## D050 — Building-only location granularity

Owner confirmed, 2026-10-27: track location at building level only. Floor and room documentation is too burdensome based on prior operational experience. Do not add optional or mandatory floor/room fields or a building/floor/room hierarchy to the V2 registration or movement experience. This settles the granularity question left open by D049; buildings remain shared across functions and entities without granting cross-scope data access. Location codes, deactivation and shared-reference maintainer authority remain open.


## D051 — Individual employee custodians

Owner confirmed, 2026-10-27: Custodian is an individual employee, not a team/department. D044's rule continues: required for In Use and optional for Available assets. The pending-directory selection in D052 is an explicit unresolved employee-assignment state, not a group custodian.

## D052 — Directory-backed employee selection with registration-pending option

Owner confirmed, 2026-10-27: use the company directory for employee selections and add a fixed/hardcoded option for employees not yet in that directory. Working display label: Awaiting employee registration; exact display wording is not prescribed by the owner. Do not interpret this as a request for a separate manually maintained employee-registration module.

The pending selection represents missing directory identity, not a synthetic account, email or approval recipient. Employee-assignment resolution and pending-item visibility must be designed. Owner follow-up confirmed the fallback is available only to Custodian. Business Owner must resolve to a real company-directory account. Do not apply the fallback to approval routing or other person fields by analogy. See `../architecture/EMPLOYEE-SELECTION-DESIGN.md` for the proposed handling and unresolved scope.


## D053 — Single Condition dropdown with owner-selected labels

Owner selected and reaffirmed, 2026-10-27: use one Condition dropdown containing exactly Good, Broken and Ready to Auction. The owner declined splitting Auction Readiness into a separate field. Do not substitute Needs Repair/Unusable or add a separate Auction Readiness field. Asset Status and request/approval progress remain separate under D045. Selecting Ready to Auction records the chosen condition; it is not evidence of completed direct disposal, a sale transaction or a newly required disposal approval. Default condition, permitted state combinations and transition/edit authority remain to be specified with the screen/operation contract. D044's application-controlled requiredness continues.


## D054 — Initial registration status and default condition

Owner confirmed, 2026-10-27: do not allow direct registration as In Use. New assets enter as Available; application registration must not expose an editable initial status that allows bypassing this rule. Default Condition to Good, using the single dropdown from D053. Good is a default, not an instruction to replace an explicitly selected permitted condition.

Moving a registered asset to In Use is a separate authorized update under existing BAU/transfer rules, with the custodian requirement and Custodian-only pending-registration option preserved. Available assets retain the confirmed optional custodian rule; this decision does not require an initial custodian or require it to be blank. Registration remains create-only and Accounting Asset Code uniqueness remains company-wide. Bulk/API registration validation should follow the same initial-state rule; a post-create assignment must not be silently bundled into registration to defeat it.


## D055 — Entity-specific Asset Type catalogues

Owner confirmed, 2026-10-27: maintain Asset Types separately for each entity. Each type belongs to an entity and retains the Category lookup from D048. The same display label may describe separate records in different entity catalogues; do not merge them into a single global type merely because their labels match. Registration must validate that the selected type belongs to the asset's entity.

Accounting categories remain the fixed KO/NK/PL classification from D047; this decision does not make categories independently editable by entity. Locations remain shared across entities/functions under D049/D050. Type-maintainer roles, duplicate rules within one entity, availability across functions, and transfer handling where the destination entity uses a different type record remain to be designed. Entity-scoped maintenance must be enforced at the mutation boundary, not only by a filtered picker.


## D056 — Asset Type catalogue maintainers

Owner agreed, 2026-10-27: Global User maintains Asset Types within its assigned entity; Super User maintains Asset Types across entities. Other roles select existing types during registration and do not independently grant type-catalogue maintenance. Role combinations retain their explicit authorized privileges; a pair-scoped Asset Manager role does not implicitly grant entity-wide reference maintenance.

Maintain the entity parent and valid Category lookup on every type. This decision settles the type-maintainer question in D055, not the authority to change Accounting's fixed categories or global shared buildings. Deactivation/reclassification safeguards and destination-type mapping for cross-entity transfers remain design details. Enforce maintenance scope in the backend as well as in the UI.


## D057 — Cross-entity destination Asset Type mapping

Owner agreed, 2026-10-27: a cross-entity asset transfer specifies a valid receiving-entity Asset Type before requesting approval. The destination type must use the same Accounting Category (KO/NK/PL) as the source. If no suitable type exists, the receiving entity's Global User creates it first; Super User's cross-entity catalogue maintenance authority under D056 remains available.

The transfer preserves asset identity and the company-wide Accounting Asset Code, with prior/new type references in history. Both required Business Owner capacities approve under D025/D027–D029 and D042; mapping does not bypass those decisions. Rejection leaves the asset unchanged. Selecting receiving-catalogue reference data does not grant access to unrelated destination assets or maintenance privileges. Revalidate destination type/entity/category and reviewed asset/request versions before applying the approved transfer.


## D058 — Provisional registration-field review

Owner response, 2026-10-27: agreed for now, to check later. Treat the following as a provisional working field contract for design, not a permanently finalized mandatory-field policy. Revisit during screen review and representative registration testing.

Provisionally required: Asset Name, Asset Type, Business Owner, Building and Condition (default Good). Provisionally optional: Serial Number, Manufacturer/Model, supporting documents/photos and Custodian while Available. Existing confirmed Accounting Asset Code, Purchase Date/Purchase Cost, authorized entity/function, IDR and Available-only initial registration rules remain in force. Business-required fields are application-validated under D044, not SharePoint Required flags. Include a visible field-review checkpoint before accepting the registration implementation; record any changes against this decision and update the screen/data contract together.


## D059 — Movement through a selected-assets list

Owner feedback, 2026-10-28: asset movements/transfers are frequent, so opening each asset detail and starting a movement separately is too burdensome. Adopt the proposed path: search item → add to list → view selected list → start movement. Interpret View as a batch-selection review, not a requirement to visit every asset detail. Keep direct detail-page actions as optional alternate entry points, not the only path.

Support collecting multiple authorized assets for a movement operation. This usability direction does not change BAU permissions, owner/scope-transfer approvals, same-person capacity handling, destination-type mapping, individual asset identity/history or required exception reasons. Common destination versus per-row changes, permitted mixed-scope selections, grouping and partial-failure application policy remain to be settled. This does not approve bulk disposal. See `../architecture/ASSET-MOVEMENT-WORKSPACE.md` for the proposed screen interaction and open questions.


## D060 — Different movement changes per selected asset

Owner confirmed, 2026-10-28: selected assets can have different movement changes/destinations within the same movement workspace. Do not constrain the list to a single common destination or require separate detail-page movement sessions for every asset. D059's search → add to list → view selection → start movement path remains the entry flow.

The proposed screen sequence is Select assets → Enter per-asset changes → Review and submit. That detailed layout, execution grouping, mixed-approval handling, partial-failure policy and final display labels remain proposals for owner review, not additional confirmed business decisions. Per-asset scope/identity/history, destination-type mapping and Microsoft approval obligations continue. See `../design/concepts/2026-10-28/asset-movement/README.md` for the visual flow proposal.


## D061 — Movement visual flow accepted as working direction

Owner response, 2026-10-28: the selected-assets/per-row movement design is close enough. Retain the Select assets → Enter changes → Review and submit visual direction for detailed implementation refinement. This is working concept acceptance, not runtime acceptance or resolution of every execution/partial-failure policy left open under D059/D060. Preserve different changes per asset, optional detail-page entry, existing permissions and Microsoft approval obligations.

## D062 — Direct-disposal interaction accepted

Owner accepted the proposed interaction, 2026-10-28: select asset(s) → choose Sale or Non-sale → enter disposal details → review → confirm. Disposal date is required in both modes. Sale requires buyer and selling price. Completion removes the disposed asset from the active register and preserves history. No disposal approval workflow is introduced. Business-required fields follow D044's application validation policy; no mandatory BAU remarks/reason is added.

The preceding question offered multiple assets versus one asset at a time, and the acceptance did not explicitly choose between those options. Keep disposal selection cardinality open; do not infer approved bulk-disposal behavior solely from this concept acceptance. Mixed sale/non-sale batches, price allocation, buyer cardinality, recovery and disposal authority remain to be specified where relevant. See `../architecture/DIRECT-DISPOSAL-DESIGN.md`.


## D063 — Single and multiple-asset direct disposal

Owner confirmed, 2026-10-28: support both single-asset and multiple-asset disposal using the same selected-assets list. This settles selection cardinality left open in D062; selection can contain one or more authorized assets without repeating separate asset-detail disposal sessions.

Retain the accepted Sale/Non-sale, required disposal date, required buyer/selling price for Sale, final review/confirmation, history and no-approval rules. Per-asset versus common batch values, selling-price representation/allocation, mixed Sale/Non-sale handling and partial-failure/recovery behavior remain open; support for multiple selection alone does not choose these policies or imply whole-batch atomicity. Validate authority/state and preserve results/history for every asset.


## D064 — Per-asset disposal details and shared-value shortcut

Owner agreed, 2026-10-28: disposal details are entered per asset. Provide an optional Apply to selected shortcut for shared values such as disposal date or buyer. Selling price remains a per-asset entry; do not infer or distribute a batch-total selling price.

Shared-value application is form preparation, not transaction execution. Show resulting per-asset values for review, allow subsequent per-asset correction, and enforce the applicable Sale/Non-sale inputs for each asset under D062. A buyer shortcut does not add a buyer requirement to Non-sale rows. Asset selection, direct-disposal authority, final confirmation, preserved history and absence of disposal approvals remain unchanged. Exact shortcut fields, overwrite interaction, mixed Sale/Non-sale support and partial-failure execution policy still require design review.


## D065 — Disposal workspace and Asset Details/History visuals agreed

Owner agreed, 2026-10-28: retain the displayed disposal workspace and Asset Details/History concepts as working visual designs. Disposal shows per-asset details, a shared date/buyer shortcut and separate selling prices. Asset Details/History shows current context, Overview/Financials/History/Documents navigation and chronological business/approval/application events. Optional single-asset Move/Dispose entry points coexist with the faster selected-assets paths.

This accepts the visual direction, not runtime outcomes or every interaction implied by generated sample controls. Unresolved buyer representation, mixed-mode/overwrite behavior, partial failures, exact permissions/history detail visibility, financial formula/initial value and production component contracts remain under their existing design gates. Generated data and actor labels remain illustrative. See `../design/concepts/2026-10-28/asset-details-disposal/README.md`.


## D066 — Visuals accompany flow proposals

Owner instruction, 2026-10-28: give a visual when proposing a flow. Future user-flow proposals should include a relevant screen mockup, storyboard or flowchart alongside concise explanation rather than text-only proposals followed by a separate offer to draw them. Keep visual proposals distinct from accepted business requirements and runtime implementation. The first stock-verification respondent storyboard is a proposal for review, not approved response-field/state policy.


## D067 — List-first stock responses with correction-only detail entry

Owner direction, 2026-10-28: stock-verification assignments may contain many assets. Use a movement-like assigned-assets list; one click marks an asset correct and a second click marks it not correct and prompts a separate screen to enter corrected observations. Correct assets do not require completing a separate per-asset questionnaire.

The corrections change only the respondent's assigned verification data/response, never the master asset register. Preserve the original assigned context and evidence history. Ordinary master updates remain a separate authorized process, including applicable transfer approvals. The proposed click interpretation is two successive activations of a visible state control (first Correct, second Needs correction/open correction form), without a timing-dependent double-click. Reversal/cancel, persistence and final submission details remain interaction design proposals for review.

This supersedes the questionnaire-first respondent storyboard as the primary path. Keep mobile-friendly access, assigned-only authorization, open-response editing and read-only historic assignments. Correct is a respondent assertion, not automatic cycle verification, master correction or Business Owner sign-off. See `../architecture/STOCK-RESPONDENT-LIST-DESIGN.md` and the linked visual proposal.


## D068 — List-first respondent concept accepted as working direction

Owner response, 2026-10-28: the revised assigned-assets list and separate correction screen are good enough; continue. Retain D067's list-first interaction and assignment-only corrections as the working respondent design. This accepts the direction, not runtime testing or every unresolved save/cancel/submission/component detail. Two deliberate activations remain the proposed timing-independent interpretation; preserve keyboard/mobile usability and visible states. Manager review and Business Owner sign-off visuals are subsequent proposals, not approved by this acceptance.


## D069 — Manager review and owner sign-off sequence accepted

Owner accepted, 2026-10-28: Asset Manager reviews evidence, records review outcomes/exceptions, previews relevant owner-specific results and requests Business Owner sign-off through Microsoft Approvals. Accept the shown manager-review/sign-off visuals as the working design. Master corrections remain separate authorized operations; approval requests do not silently update master data. Each owner receives only relevant results, and unresolved assets remain unverified even when acknowledged for closure under D035.

Detailed review-state vocabulary, verification criteria, change/reapproval rules, exact submission/closure gates, persistence, permission enforcement and production components remain implementation/design tasks, not runtime acceptance. The illustrative data, checkbox and controls do not prove deployed behavior. See `../architecture/STOCK-VERIFICATION-REVIEW-DESIGN.md` and its visual links.


## D070 — Apply reconciliation corrections before final sign-offs

Owner confirmed, 2026-10-28: upload → compare/review → authorized Asset Manager explicitly previews and applies eligible corrections → configured Accounting and Governance final sign-offs through Microsoft Approvals. Final sign-off reviews the actual applied results and retained evidence, rather than authorizing a future reconciliation apply step. This supersedes only the ordering in D038 and subsequent summaries, including D042; retain D036 provenance, D037 configured assignments and D038 explicit application/audit requirements.

Business Owner approvals required for owner/scope transfers still precede those specific transactions. Reconciliation does not bypass registration, direct-disposal, field-edit or financial controls. Book Value remains governed by D046's deferred monthly formula, with no automatic ledger overwrite. Keep application outcomes separate from final certification; an applied run awaiting final sign-off must be shown honestly. Final rejection/rework/rollback handling and eligibility with unresolved follow-ups remain open policy decisions. The revised visuals illustrate this ordering, not approval of every field or readiness rule.


## D071 — Reporting progress flow and visuals accepted

Owner accepted, 2026-10-28: Reports → Request progress → Scoped process detail → Review outcomes/activity → Export authorized data or send an eligible standard reminder to relevant pending respondents. Accept the two reporting-progress visuals as the working design. Business Owners can monitor relevant owned-asset work initiated by others; unrelated records, counts and activity remain inaccessible. Retain the existing role/assignment scope and historical read/export boundaries; this creates no additional role or approval authority.

Keep workflow stage, response, review/verification, transaction application and final sign-off separate. Reconciliation retains D070 application before final sign-off, and asset owner/scope transfers retain their prerequisite approvals. Reminders do not change responses or business status; Microsoft Approvals remains the decision surface. Exact metrics, deadlines, report fields, export formats/download controls, reminder channel/rate limits, historical visibility and Power BI/refresh architecture remain open. Acceptance is of the flow/visual direction, not implementation, runtime testing or every illustrative control/status. See `../architecture/REPORTING-PROGRESS-DESIGN.md` and its linked visuals.
