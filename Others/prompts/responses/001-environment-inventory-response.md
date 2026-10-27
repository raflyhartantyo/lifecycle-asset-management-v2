# ENV-INVENTORY-001: Company environment inventory (read-only)

## Task

Collect the read-only company environment inventory for Lifecycle Asset Management, and identify approved test identities and setup dependencies. Report each item as AVAILABLE, MISSING, or UNKNOWN, with the evidence used.

## Required repository references

- `Others/handover/COMPANY-ENVIRONMENT-INVENTORY.md`
- `Others/testing/SETUP-CHECKLIST.md`
- `Others/testing/PERSONA-BINDINGS.csv`
- `Others/testing/fixtures/` (file list only)
- `Others/requirements/PHASE-1-REQUIREMENTS.md`, `Others/requirements/PERMISSION-MATRIX.md`, `Others/decisions/DECISIONS.md` (presence checked only)

## Authorized scope

- Read-only access to the public repository `raflyhartantyo/lifecycle-asset-management-v2`.
- No access to any company environment, Power Platform tenant, SharePoint site, or Power BI workspace.
- No provisioning, no account or fixture creation, no test execution, no notifications.

## Completion criteria

- Each of the six inventory topics is marked AVAILABLE, MISSING, or UNKNOWN, with evidence or the read-only step the operator should take.
- Persona identities are listed by alias, with their availability status.
- Missing and unknown prerequisites are listed, with the role that can resolve each.
- A readiness summary states which testing is blocked.

## Method

- Read the two required documents directly from `raw.githubusercontent.com` on branch `main`.
- Read the GitHub API for the commit, releases, folder listings, and file presence.
- Read `PERSONA-BINDINGS.csv` (13 personas).
- No company system was contacted.

## Completed

| Item | Result |
|---|---|
| Repository accessible | AVAILABLE. Public repo, default branch `main`. |
| Commit recorded | `59d7254077af12fb74b305e5472852995f2dc32e` (2026-10-27 16:52 UTC, `main` head). |
| Required documents read | Both documents read in full. |
| Baseline files present | Present (HTTP 200). Content not reviewed. |
| Persona bindings read | 13 personas. None has an approved alias. |
| Fixture files listed | 8 files in `Others/testing/fixtures/`. Contents not read. |

## Evidence

- Repo commit: GitHub API `commits/main` returned the SHA and date above.
- Releases: none. The `baseline-001` tag named in the README is not a GitHub Release. Git tags not checked.
- Persona file: 13 rows, all `Provisioned = NO`, `Company_Approved_Identity_Alias` empty.
- Fixture folder: `ASSETS.csv`, `FIELD-MAPPING.csv`, `IMPORT-SCENARIOS.csv`, `INACTIVE-ASSETS.csv`, `INVENTORY.csv`, `README.md`, `RECONCILIATION-SCENARIOS.csv`, `SCOPES.csv`.

## Inventory status

### A. Repository baseline

| Item | Status |
|---|---|
| Repo accessible | AVAILABLE |
| Commit recorded | AVAILABLE (`main` head, not confirmed as the baseline) |
| Baseline files present | AVAILABLE (presence only) |
| Baseline commit confirmed | UNKNOWN |
| `baseline-001` tag | UNKNOWN |
| Delivered app and flow versions | UNKNOWN |

### B. Company environment (six topics)

| Topic | Status | Read-only step for the operator |
|---|---|---|
| 1. Environments and deployment | UNKNOWN | Power Platform admin center: list environments, type, Dataverse status. Check solution membership. Admin confirms licence and connector limits. |
| 2. Apps and flows | UNKNOWN | Maker portal: names, last modified, enabled or disabled, app checker results. Confirm whether both reconciliation variants and the helper flows exist. Read definitions and run-history metadata only. Do not run flows. |
| 3. SharePoint metadata | UNKNOWN | List settings: column names, types, required, indexes, approximate counts. Confirm the `Master_Asset2` binding. Metadata only. |
| 4. Existing authorization | UNKNOWN | Site, report, and flow permissions, recorded as group labels only. Check whether direct list access bypasses app filters. |
| 5. Scale and usage | UNKNOWN | Owner estimates: users, concurrency, devices, asset and inventory counts, retention. |
| 6. Brand, media, Power BI | UNKNOWN | Confirm approved logo, icon, and font assets. Confirm Power BI workspace, report, dataset, and permissions. Reference secrets by alias only. |

### C. Test identities

| Item | Status |
|---|---|
| Bindings file present | AVAILABLE |
| Approved identity aliases | MISSING (0 of 13) |
| Super-user identity (`SUPER`) | MISSING. Admin-level, cannot prove restricted access. |

Personas and scopes:

| Persona | Role | Scope |
|---|---|---|
| OP_A | Asset operator | UAT-ORG-A / UAT-FNC-A1 |
| INV_A | Inventory operator | UAT-ORG-A / UAT-FNC-A1 |
| MGR_A | Asset manager | UAT-ORG-A / UAT-FNC-A1 |
| BO_A | Business owner | UAT-ORG-A / UAT-FNC-A1 and A2 |
| BO_B | Business owner | UAT-ORG-A / UAT-FNC-A1 and UAT-ORG-B / UAT-FNC-B1 |
| VIEW_A | Viewer | UAT-ORG-A / UAT-FNC-A1 |
| RESP_A | Respondent | UAT-ORG-A / UAT-FNC-A1 |
| RESP_B | Respondent (replacement) | Assigned replacement task |
| GLOBAL_A | Global user | UAT-ORG-A, all functions. No B. |
| SUPER | Super user | Application-wide |
| ACC_A | Accounting approver | Reconciliation run in A / A1 |
| GOV_A | Governance approver | Reconciliation run in A / A1 |
| NO_ACCESS | No grant | None |

Distinct-identity needs (the same operator can run these sequentially, but they need separate approved identities to be certified):
- Prior and replacement respondents (RESP_A, RESP_B): 2 identities MISSING.
- Business owner paths (BO_A, BO_B): 2 identities MISSING. Which one is outgoing and which is incoming is UNKNOWN. The bindings file does not say.
- Accounting and governance approvals (ACC_A, GOV_A): 2 identities MISSING.
- Assigned versus unassigned (NO_ACCESS against an assigned persona): 1 identity MISSING.

### D. Fixtures

| Item | Status |
|---|---|
| Fixture files in repo | AVAILABLE |
| Fixture completeness | UNKNOWN (not read) |
| Fixtures in company environment | UNKNOWN (not created; blocked) |

Required per checklist: 2 entities, 3 functions, 7 active and 1 inactive assets, quantity inventory.

### E. Notifications and connections

| Item | Status |
|---|---|
| Approved notification destinations | UNKNOWN. Flow owner to confirm. |
| Connections per flow | UNKNOWN. Maker to list per flow. |

## Missing or unknown prerequisites

| Prerequisite | Status | Resolved by (role) |
|---|---|---|
| Environment list and Dataverse status | UNKNOWN | Power Platform admin |
| Solution membership and deployment method | UNKNOWN | Solution owner or admin |
| App and flow versions and checker results | UNKNOWN | Maker or app owner |
| SharePoint list metadata | UNKNOWN | SharePoint site owner |
| Authorization groups and report access | UNKNOWN | Site and workspace admins |
| 13 approved test identity aliases | MISSING | Company identity or access team |
| Distinct approval identities (respondents, business owners, accounting, governance) | MISSING | Access team. Approvals by business owners. |
| Outgoing and incoming owner mapping | UNKNOWN | Main developer |
| Notification destinations | UNKNOWN | Flow owner |
| Fixture completion | UNKNOWN | Test operator and main developer |
| Approved brand assets | UNKNOWN | Brand team or GCO |
| Power BI workspace and dataset | UNKNOWN | Power BI workspace admin |
| Scale estimates | UNKNOWN | Business owner |
| Prior app and flow copies for rollback | UNKNOWN | Maker |
| Baseline commit and `baseline-001` tag | UNKNOWN | Main developer |

## Blockers

- **Persona-based functional cases:** blocked, no approved aliases.
- **Distinct-identity cases:** blocked. A single operator cannot certify these.
- **Email, Teams, and approval cases:** blocked, no confirmed notification destinations.
- **Fixture creation in company environment:** blocked, environment and identities not available.
- **Power BI checks:** blocked, workspace and dataset not confirmed.
- **Rollback steps:** blocked, prior app and flow copies not confirmed.

## Readiness summary

- Company-side topics confirmed AVAILABLE: 0 of 6.
- Repo-side items AVAILABLE: repo, commit, file presence, persona file, fixture file list. None of these proves the company setup.
- Ready to run: none.

## Not done

- No company environment, SharePoint list, flow, or Power BI item was inspected.
- The contents of the three baseline files, the fixture files, and the flow definitions were not reviewed.
- No account, fixture, or test was created or run.
- No credentials were requested or recorded.

## Next steps

1. Operator completes the read-only steps in section B and returns evidence.
2. Main developer confirms the baseline commit, the `baseline-001` tag, and the outgoing and incoming owner mapping.
3. Access team issues approved aliases for the 13 personas, including the distinct approval identities.
4. Fixture creation and test execution need a separate instruction after these are complete.
