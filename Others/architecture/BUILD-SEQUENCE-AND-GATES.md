# Build sequence and evidence gates

Status: proposed engineering delivery sequence following confirmed target scope through D072. This does not create a dated rollout commitment or authorize company configuration changes. Existing backlog IDs remain stable; slice IDs below group the work for implementation.

D072: the tables describe design dependencies and prerequisites before executing/testing a feature. They do not require tenant observations before architecture/resource preparation. The owner handles actual access/connector setup at implementation time. Continue with [the solution/connector architecture](SOLUTION-AND-CONNECTOR-ARCHITECTURE.md), schemas and operation contracts now; general capability prompts are deferred.

## Proposed delivery slices

| Slice | Deliver together | Entry gate | Exit evidence / existing test mapping |
| --- | --- | --- | --- |
| S0 — architecture contracts | Connector/access requirements, list contracts, identity/persona binding placeholders, first query/mutation/evidence contract | Accepted business scope; record unknown bindings as implementation dependencies | Reviewable architecture/schema/operation specifications; actual configuration and test identities bound during implementation; BL-01/02/03 |
| S1 — app shell and reference reads | Brand tokens/components, entry/context, safe navigation, scoped reference queries, loading/error/freshness | Enough access/reference schema and backend isolation to test real reads; disconnected UI can precede this | Company-run ordinary/Global/Super/no-access and context-change checks; applicable AUTH/UX; BL-04 and reference part of BL-05 |
| S2 — first asset slice | Reference maintenance within authority, guided registration, asset search/detail/history; then create-only import | SITE-F dedicated LAM resources and bindings; tag allocation, field review, unique-code enforcement and initial financial-value behavior defined | Real authorized single create/read/history and denied direct-call tests; import preview/error/retry checks; REG/AUTH/UX; BL-05 |
| S3 — movement | Selected-assets workspace, per-row changes/review, BAU writer, transfer requests/Microsoft Approvals, results/history | Asset slice; approval provisioning/configuration; batch/grouping/version/retry policy | Routine and dual-owner/same-person/rejected/failed-apply paths; shared type/Category consistency under D074; MOV-01..08 plus new implementation-specific batch checks; BL-06 |
| S4 — disposal and quantity inventory | Direct-disposal workspace/writer/history; separate quantity register/transfer writer/history | Disposal and inventory contracts; field/state/concurrency and partial-failure policies | Single/batch Sale/Non-sale, active-register exclusion only after success, retained history, unauthorized calls, valid quantities; DIS/INV and implementation-specific cases; BL-07/08 |
| S5 — stock verification | Cycle/assignment setup, list-first responses/corrections, manager review, owner-specific sign-off, reminders/history | Register/scope/people, response-state/verification/readiness contracts and approval configuration | Assigned-only current/history access; no automatic master writes; exceptions stay unverified; SO-01..11 plus accepted list-interaction cases; BL-09 |
| S6 — finance and reconciliation | Defined monthly calculation first where comparison needs its values; ledger compare/review, explicit eligible apply, actual-result final sign-offs | Formula/period/initial-value contract where used; ledger/field eligibility; final rejection/rework and follow-up readiness rules | Formula/period/retry cases to be authored after finance specification; REC-01..07 plus stale/conflict/snapshot cases; BL-14/10 |
| S7 — complete reporting | D071 progress/detail views, approved overview/history metrics, protected exports, freshness/refresh contract | Each producing slice's scoped data/outcome contract; metrics/export/reminder details | Mixed-owner subset isolation, direct URLs, historical export, correct reminders and honest refresh outcome; RPT-01..06, UX; BL-11 |
| S8 — acceptance and release | Integrated regression, migration decision/rehearsal, recovery rehearsal, release record, staged onboarding | All required first-release slices, company deployment/support authority, required tests executable | Owner-run acceptance evidence; no unresolved Critical/High defects; blocked required gates resolved; promotion/cutover records; BL-12/13 |

Slice order reflects dependencies, not a requirement to finish unrelated work before starting it. Quantity inventory can progress once its own foundation is ready. Reporting query/scope contracts and basic progress views accompany the first process slice; S7 consolidates the full experience. Audit and recovery accompany every mutation from S2 onward. Do not defer all authorization, reporting correctness or per-flow checks to S8.

The monthly calculation is explicitly retained by D046. The formula is deferred, not canceled. An unimplemented or invented financial value must not be presented as production-ready registration/reconciliation. Keep nonfinancial design work moving while the financial contract remains pending.

## First contract package to prepare

1. Specify backend identity and access enforcement requirements: how each read/write is authenticated; ordinary pair, Global entity, Super and task/history subsets; direct SharePoint/flow access; service-connection boundaries and revocation.
2. Define the exact Access/Approver configuration and required reference contracts. Organizations/Functions already have a [creation guide](../sharepoint/v2/CREATION-GUIDE.md); do not recreate baseline lists blindly.
3. Define registration/read/history operation contracts: company-wide unique Accounting Asset Code under concurrent submissions; LAM tag allocation; D058 field review; Available/Good defaults; directory/pending Custodian; field/provenance/audit and initial finance behavior.
4. Define the app shell's actual query/operation bindings, shared components, error/result model and authorized context-switch behavior. Test chosen contracts with synthetic scopes before broader writers.
5. Deliver a concrete first slice with complete files and manual guidance. Company setup that is not yet available is a named dependency, not a fictional passed test.

No new business questions are inferred as settled by this checklist. Use the accepted decisions where they already answer a question. Ask only for remaining material policy/company facts when the relevant contract genuinely needs them.

## Definition of ready for a feature delivery

- Its accepted requirements and unresolved gates are identified; required business policy for the delivered actions is settled.
- Exact data/internal names, caller identity, row/field scope, operation validation and relevant state transitions are specified.
- Current source/replacement commit and logical resource/connection aliases are documented. Actual company bindings and approved test identities/sinks are configured when implementing/testing the affected feature, with unknowns explicit.
- Old/new preview, mandatory application validation, failures/conflicts, duplicate/uncertain requests and recovery behavior are concrete.
- Screens/formulas/flow resources and manual steps are reviewable, with expected outcomes and rollback boundaries. A mockup alone is not an implementation package.

## Definition of done for an implemented slice

- The user has implemented the identified resource version and reported actual Studio/flow/runtime evidence.
- Required positive and negative scope tests pass through UI and approved backend test paths; hidden buttons alone are insufficient.
- Persisted business outcomes, evidence and retries match the contract. Partial failures do not become false batch success.
- Relevant desktop/mobile/keyboard/contrast/label tests are complete; real-device evidence is distinguished from emulation.
- Changed resources, configuration, handover, mapped cases/results, defects and recovery/rollback guidance are versioned in GitHub.
- Missing required evidence stays NOT RUN/BLOCKED, rather than being converted into acceptance from a screenshot or source check.

## Per-slice file delivery

| Folder | Expected feature resources |
| --- | --- |
| Power Apps / app folder | Complete affected app/screen/component resources; binding/formula instructions; screen index; validation and rollback; exact target-versus-baseline status |
| Power Automate / each affected flow folder | Complete implementation resource; trigger/input/output contract; configuration/bindings; manual steps; action/decision paths; validation and recovery/rollback |
| Others | Exact schema/permission contract, accepted decisions, visual/spec links, change/release record, cases/evidence templates and a PENDING company-Claude transfer prompt when ready |

For every new prompt include Q&A-only context, the user's manual actions, expected evidence and the concrete `Others/prompts/responses/<ID>-<topic>-response.md` return path using [TEMPLATE.md](../prompts/TEMPLATE.md). The user pastes the returned Markdown into GitHub and sends the link. Do not assume Claude can open the repo or inspect company systems.

Keep baseline files intact. A plain flow definition or concept YAML is not evidence of a genuine importable package. Identify each file's actual use and compatibility in its handover; tested company export/import packages are separate release evidence.

## Implementation setup dependencies — owner handled

D073 selects SITE-F, the existing Function site, instead of the unavailable dedicated SITE-A plan. Actual rights on SITE-F are not supplied; earlier site permission observations are not carried over. Follow [the shared-site setup](../sharepoint/v2/SHARED-FUNCTION-SITE-SETUP.md) for new LAM resources while preserving host content/membership. ENV-A has the blank new app; no isolated test environment is confirmed. ENV-B exists but its suitability/access is unknown. Approvals availability/provisioning, connection identities, licenses/policies and notification recipients require company evidence already described in the [Approvals integration design](APPROVALS-INTEGRATION-DESIGN.md). Do not create production-like notifications or assume isolation from a development label.

Continue site-independent specification and UI preparation now. The existing [PENDING foundation prompt](../prompts/PENDING-002-sharepoint-foundation.md) can be used when implementing the new LAM lists on SITE-F; this blueprint does not instruct the user to execute it early. General inventory/access prompts 001 and 003 are DEFERRED under D072; no report is requested. Future prompts support concrete delivered implementation work when useful. Setup dependencies do not block preparing the architecture, schema and app/flow contracts.
