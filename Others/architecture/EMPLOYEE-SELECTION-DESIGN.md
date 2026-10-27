# Employee selection and pending directory registration

Status: directory source and Custodian-only pending option confirmed D051/D052; physical contract pending. No company directory was queried and no application/source connection was added.

## Confirmed

Custodian represents an individual employee. Use company directory selection, with a hardcoded option for an employee who is not yet registered in that directory. The owner confirmed this fallback is for Custodian only; Business Owner requires a real directory account. This is a fallback selection, not an independently managed employee master or an account-provisioning request.

## Proposed representation

Display Awaiting employee registration alongside directory results. Keep an explicit pending flag/state separate from the nullable real directory identity; the final field types and stored code follow in the data contract. Do not fabricate an Entra ID, email address, SharePoint Person value or shared service account for the placeholder. The common option is not itself an individual, and multiple pending assets must not be assumed to belong to the same future employee.

Normal Available/In Use custodian requirements remain in force. For the confirmed fallback to be usable on an In Use asset, the application needs an explicit pending-employee exception to the ordinary resolved-person validation. That is the proposed interpretation to validate in the screen contract, not permission to silently mark an unknown identity as registered.

Propose a visible pending badge and an operational list of assets needing resolution. When the employee becomes searchable, an authorized operator explicitly selects the actual directory account, retaining prior/new assignment and actor/time in history. Do not silently match accounts by display name or automatically replace every pending selection with the same employee. No additional mandatory free-text reason is introduced for this routine resolution.

Historical references should preserve an identity/display snapshot when available; directory account changes or removal must not erase recorded business history. Directory membership is not an app role grant. The fallback does not provide login, access-matrix permissions, assigned tasks or authority to approve.

## Approval boundaries and open choices

The fallback is restricted to Custodian. Business Owner selection must reject a pending placeholder and require a real directory account. Microsoft Approvals routing additionally requires a real, authorized, routable approver identity; a pending custodian cannot receive an assigned response task or approve. Directory presence alone does not grant Business Owner approval authority. Do not substitute the maker, initiator, Asset Manager or a shared account without an approved routing rule.

Who resolves pending assignments, whether extra identity hints are useful/optional, permitted directory search scope, inactive/guest account handling and exact pending display wording remain screen/configuration details. No software-specific alternate form or account-provisioning feature is added.

## Validation to supply with implementation

Directory selection; pending selection; pending-to-real correction with audit; concurrent correction; unavailable directory lookup; repeated names; directory account removal/history; no task/approval routed to a placeholder; pending identity grants no access. Include confirmation that the fallback is visible for Custodian and unavailable/rejected for Business Owner. All runtime checks NOT RUN.
