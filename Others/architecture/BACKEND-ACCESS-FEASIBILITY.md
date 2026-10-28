# Backend access feasibility — Microsoft findings and LAM recommendation

Checked against official documentation on 2026-10-28. Platform facts below are separate from the proposed LAM architecture. No company tenant, licensing, permissions or connections were inspected.

## Verified platform facts

1. SharePoint lists/libraries inherit parent permissions by default; unique list/item permissions can break that inheritance. Permission configuration is a separate task from app filtering. [Microsoft: permission levels and inheritance](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels).
2. SharePoint supports 50,000 unique security scopes per list/library, with a recommended general limit of 5,000. This measures permission scopes, not the number of assets or the list-view threshold. [Microsoft: SharePoint limits](https://learn.microsoft.com/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).
3. Individually sharing items creates distinct scopes even when the assigned permissions are identical; inherited folder permissions can share one scope. Grouping strategy and growth matter. [Microsoft: managing permission scopes](https://learn.microsoft.com/en-us/sharepoint/manage-permission-scope).
4. Instant flows can have run-only users who can trigger but cannot edit the flow. The owner can choose caller-provided connections or existing flow connections. This configures invocation/connection use; it does not by itself establish LAM's row/action authorization. [Microsoft: sharing a cloud flow](https://learn.microsoft.com/en-us/power-automate/create-team-flows).
5. App sharing and resource/connection sharing have separate requirements, depending on the resource. Company bindings must be inspected rather than assumed from the ability to open an app. [Microsoft: share canvas-app resources](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/share-app-resources).

These sources do not establish a trustworthy LAM caller-identity expression for an elevated Power Apps-triggered flow. No undocumented trigger header, app-passed email or service account profile is accepted as that proof. The selected mechanism must be documented and demonstrated in the company configuration.

## LAM inference and recommendation

At approximately 5,000 assets, giving every asset independent permissions would approach the recommended scope count before considering more assets, assignments, documents or history. This is a planning inference, not evidence that the company has hit a platform limit. Ten to thirty users does not remove the scope-growth issue.

| Candidate | How it could enforce the contract | Remaining proof required | Recommendation status |
| --- | --- | --- | --- |
| Controlled service reads/writes, protected SharePoint | Authenticated backend checks roles/participation, scopes queries and projections, validates all mutations; ordinary users lack broad direct data access | Trusted caller mechanism; service permissions; run-only/configuration boundaries; query/paging/performance; connection continuity and licensing/policy | Leading candidate to evaluate; not selected or creation-ready |
| Native SharePoint-scoped reads plus controlled writes | SharePoint ACLs restrict direct rows; controlled writer validates business actions; separate projections/snapshots cover restricted fields/history | ACL and group model, update/revocation consistency, owner/task projections, scope-growth budget, direct-list/download tests and secure writer identity | Alternative if company supports and tests the full design |
| Broad site/list access plus app filters | Restricts the presented UI only | Does not establish backend denial for copied URLs/direct requests or alternative clients | Does not meet confirmed requirements |

This does not select Dataverse/custom APIs/premium connectors or authorize a service account. If the company's permitted mechanisms cannot prove the required boundaries, report the gap and revisit the implementation mechanism with concrete company facts. Do not silently weaken the scope model.

## Prototype acceptance evidence before choosing

Use a company-approved synthetic scratch setup only after explicit test-scope authorization; this document and the companion prompt currently request observation only. Demonstrate:

- Distinct ordinary A/A1, B/B1, Business Owner subset and task-only identities are resolved from trusted authentication; changing submitted identity arguments cannot impersonate another principal.
- Direct SharePoint/connector/flow invocation cannot broaden reads or writes. Site membership, inherited access, sharing links, flow co-ownership and service rights are accounted for.
- A service can perform only the allowed validated operation and returns only permitted fields/rows. Client-supplied keys, query text or arbitrary list/column names cannot turn it into a general proxy.
- Current grants and workflow versions are revalidated at execution. Revocation, request retries, permission-change races and partially failed outcomes have explicit behavior.
- Mixed-owner process summaries, attachments, history and exports remain restricted through direct links, not only the app.
- Queries, counts and paging cover the expected workload and history growth without returning a misleading first page or fetching unrestricted data into the app.
- The company records approved connection identities, ownership/backup, licensing/policy and operational recovery. Sharing/run-only availability alone is not a completed authorization design.

All prototype checks are NOT RUN. The [access contract](ACCESS-AND-AUTHORIZATION-CONTRACT.md) remains the business-rule evaluation target for either viable approach.
