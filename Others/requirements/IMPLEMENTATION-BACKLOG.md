# Prioritized implementation backlog

Status: proposed execution plan, not implemented functionality or dated commitments. P0 resolves architecture foundations; P1 completes the first production replacement; P2 is the staged launch after acceptance, not removal of first-release scope.

| ID | Priority | Deliverable | Depends on | Completion evidence | Test reference |
|---|---|---|---|---|---|
| BL-01 | P0 | Company facts and deployment strategy | DEP-01/02 | Inventory verified; environment/configuration and solution/packaging approach documented. | AUTH-01,OPS-03 |
| BL-02 | P0 | Data contracts and scope model | BL-01 | Ordinary pair, Global entity, Super application and task/history/report scopes; concrete schema/internal names and authorization design. | AUTH-01..09,RPT-05 |
| BL-03 | P0 | UAT personas, fixtures and evidence setup | BL-01/02 | Approved identities/sinks; mapped synthetic scopes/data; blocked tests explicitly recorded. | Setup checklist |
| BL-04 | P0 | Zurich design system and app foundation | BL-02 | Approved assets/tokens/components, identity/session, safe scope selection, navigation and error/progress conventions. | AUTH,UX |
| BL-05 | P1 | Master data and asset browse/register/import | BL-02/04 | Create-only validated registration/import; no overwrite; scope and provenance/audit. | REG-01..06 |
| BL-06 | P1 | BAU movement and owner/scope transfers | BL-05 | Dual owner capacities, same-person explicit decision, reject/no-change and automatic history. | MOV-01..08 |
| BL-07 | P1 | Direct disposal | BL-05 | Sale/non-sale date/applicable fields; archive/history and safe failure recovery; no retired request process. | DIS-01..04 |
| BL-08 | P1 | Quantity inventory | BL-02/04 | Scoped quantities/transfer/history without asset-style owner approvals; concurrency protection. | INV-01..04 |
| BL-09 | P1 | Stock verification and participation | BL-05/06 | Access-derived cycles/filter/default due; assigned evidence/history/export; discrepancy review, reminders, owner sign-off and visible exceptions. | SO-01..11 |
| BL-10 | P1 | Accounting reconciliation | BL-02/05/06; BL-14 for formula-derived comparisons | Validated comparison/provenance, explicit authorized correction application, then configured Accounting/Governance final sign-off on actual results (D070). | REC-01..07 |
| BL-11 | P1 | Reporting/export and report-scope enforcement | BL-02/09/10 | D071 scoped process progress/detail, authorized exports and eligible standard respondent reminders; role-scoped rows/fields/counts and freshness; direct report permissions verified. | RPT-01..06 |
| BL-14 | P1 | Monthly Book Value calculation | BL-02/05; approved D046 finance contract | Versioned start-of-month formula execution, per-asset inputs/results, precision/period rules and retry/recovery; no invented formula or automatic ledger overwrite. | Finance cases pending formula/contract; author before implementation |
| BL-12 | P1 | UAT, migration rehearsal and release recovery | BL-03..11; BL-14 | All retained workflows/evidence, migration reconciliation/rollback, Zurich/accessibility/device gates and no unresolved Critical/High defects. | All required target cases |
| BL-13 | P2 | Pilot and staged onboarding | BL-12; promotion/support authority | ORG-01/IT pilot then accepted CRESS/entities; monitor defects/adoption and verify cutover records. | Approved candidate regression subset |

Every feature delivery contains complete affected app/flow files, change/implementation/configuration guidance, mapped test cases and rollback instructions. The project owner manually implements and tests; company Claude provides Q&A from supplied material and the owner returns evidence. Core test IDs above are groups/ranges, not a declaration of runtime completion. Resolve unknown contracts before applying fixtures or enabling production flows.

Delivery slices and readiness/acceptance evidence are specified in [BUILD-SEQUENCE-AND-GATES.md](../architecture/BUILD-SEQUENCE-AND-GATES.md), with [screen contracts](../architecture/SCREEN-IMPLEMENTATION-MAP.md). BL-14 makes the already-confirmed D046 monthly calculation explicit; it adds no financial policy and is included in BL-12 acceptance. Existing test IDs remain unchanged; finance-specific cases follow the deferred formula specification.
