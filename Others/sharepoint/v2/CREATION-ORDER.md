# V2 creation order

Only stage 1 has creation-ready field contracts in delivery 001. Stage 2 now has a [draft principal/grant field proposal](ACCESS-GRANT-COLUMNS-DRAFT.csv) and [authorization evaluation contract](../../architecture/ACCESS-AND-AUTHORIZATION-CONTRACT.md); these are not creation instructions. Resolve [backend feasibility](../../architecture/BACKEND-ACCESS-FEASIBILITY.md) before creating or populating authorization data. Stages 2–7 name planned responsibilities rather than final physical list names/counts. Their proposed logical relationships and fields are now in [the operational model](../../architecture/OPERATIONAL-DATA-MODEL.md) and [OPERATIONAL-DATA-CONTRACT.json](OPERATIONAL-DATA-CONTRACT.json); physical mappings follow each feature delivery, without making tenant observations a design prerequisite under D072. Do not create operational lists from the baseline column inventories.

| Stage | Data responsibility | Prerequisite / status |
| --- | --- | --- |
| 1 | Organizations, then Functions | Ready to create empty on completed SITE-A using this guide |
| 2 | Access grants, privileged administration and workflow approver configuration | Design after confirming available backend identity/permission mechanisms; enforce ordinary pair, entity Global User and application Super User scopes |
| 3 | Categories, asset types, locations and needed people references | Parent scope contracts and approved identity model; creation definitions to follow |
| 4 | Asset register, quantity inventory and their movement/disposal history | References and server-side mutation/access enforcement; no separate disposal request/approval list |
| 5 | Transfer requests, participants/decisions; stock cycles, assignments, evidence and owner sign-offs; reconciliation runs, ledger differences, sign-offs and correction outcomes | Registers and approved workflow contracts; retain historic assigned access |
| 6 | Durable audit, import outcomes, operation retry/concurrency state, notification history and reporting/export dependencies | Specify together with the operations that produce them; do not activate writers before durable evidence/recovery exists |
| 7 | Approved synthetic setup and application connections | Required schema/configuration completed, identity bindings and notification sinks confirmed; then staged app/flow implementation and tests |

Creation dependency order is not permission to activate workflows. Audit/recovery is required from the first working mutation, not an optional final feature. SharePoint reference relationships enforce parent consistency only; access control must be verified separately against AUTH test cases. A client-side filter is not a backend boundary.

Scale planning uses up to 2,500 assets per entity, approximately 5,000 assets overall, 15 inventory types, up to 30 users, 3–5 concurrent users and 6–9 function pairs across 3 entities. Inventory quantity has not been confirmed. Transaction/audit history grows independently. Follow [SCALE-AND-QUERY-REQUIREMENTS.md](SCALE-AND-QUERY-REQUIREMENTS.md) before finalizing operational lists.
