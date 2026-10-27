# Assumptions and dependencies — Phase 2 entry

Confirmed decisions remain in ../decisions/DECISIONS.md. The entries here are not additional approved business policy.

| ID | Item | Status / needed evidence | Impact |
|---|---|---|---|
| DEP-01 | Company environments, licensing, DLP/connector/solution support | Company inventory pending | Determines supported ALM/deployment and backend options |
| DEP-02 | Real list/internal-column types, indexes, lookups and data-source GUID bindings; Master_Asset2 purpose | Company metadata pending; baseline type cells blank | Data contracts, provisioning, delegation and safe migration |
| DEP-03 | Backend enforcement for tuple/entity/application scopes and task/history/report visibility | Architecture decision pending | Required authorization-negative tests cannot pass on UI filtering alone |
| DEP-04 | Approved test identities and notification sinks; actual synthetic fixture mapping | Solo-UAT setup pending | Separate-owner/unassigned/reassignment tests require actual approved identities and permissions |
| DEP-05 | Approved Zurich logo/icons/fonts/media and supported device/browser capabilities | Company inventory pending | Brand and responsive/accessibility acceptance |
| DEP-06 | Accounting schema, grouping/duplicate keys, correction field eligibility and approval routing/substitutions | Baseline comparison plus company contract review | No silent assumptions about ledger truth, automatic mutation or approval authority |
| DEP-07 | Source-data integrity, migration mapping, retention policy and cleanup/cutover expectations | Company data metadata/policy pending | Preserve existing IDs/history; no invented retention duration or unexplained-row deletion |
| DEP-08 | Measured volume/concurrency/network and numerical performance targets | Evidence/architecture review pending | No committed latency/SLA or false performance pass |
| DEP-09 | Fixed go-live date | Not supplied | Schedule remains dependency-based |
| DEP-10 | Post-launch support and production-promotion authority | Not supplied; sole UAT tester confirmed | Do not infer operational/legal company authority from test ownership |
| ASM-01 | Reviewable custodian/location-PIC respondent prefills | Traceable baseline/design assumption | Consolidated design review; no new broad participation grants |
| ASM-02 | Naming, canonical statuses, concurrency/retry/idempotency, failure visibility and component behavior | Engineering design within confirmed business rules | Document architecture decisions and verify rather than reopen routine interviews |
| ASM-03 | Registration/disposal/master-data field validation not superseded by owner choices | Carry baseline evidence as labeled draft; resolve data contracts | Do not silently treat every existing bug/rule as approved V2 behavior |

Owners: company operator/administrator supplies facts; main developer proposes architecture and fixtures; project owner reviews material business conflicts and performs UAT. Company Claude assists within its actual permitted tools.
