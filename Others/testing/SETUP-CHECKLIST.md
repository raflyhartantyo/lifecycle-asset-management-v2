# Individual-testing setup checklist

Complete in a company-approved development/test environment with company-approved access. This checklist is not a provisioning script or instruction to change production.

- [ ] Record repository commit and delivered app/flow deployment versions; distinguish baseline reference from target V2 implementation.
- [ ] Obtain/verify the company environment inventory, target list internal names/types, connections and approved notification sinks.
- [ ] Identify the single test operator and available approved test identities. Fill PERSONA-BINDINGS.csv using aliases; retain actual credentials privately in company-managed authentication.
- [ ] Provision access through the actual permission system, including SharePoint/report/flow enforcement; a changed UI label is insufficient.
- [ ] Use isolated browser profiles/private sessions for different approved identities; check displayed identity, effective roles and active scope before every case. Clear cached sessions after role changes according to the delivered policy.
- [ ] Distinct-identity paths need distinct approved identities: outgoing versus incoming owners, assigned versus unassigned users and prior versus replacement respondents. The same operator can exercise them sequentially. Never borrow credentials or bypass company identity controls.
- [ ] If only one approved identity exists, run permitted sequential role/configuration checks in development and label their limitations. Separate-identity cases stay BLOCKED; UI simulations remain UI checks and cannot certify authorization or independent approvals.
- [ ] Bind all email/Teams/approval outputs to controlled test destinations; check embedded recipients/links/campaign text before any run.
- [ ] Complete fixture FIELD-MAPPING.csv; create two entities/three functions, approved reference data and seven active/one inactive synthetic assets plus quantity inventory. Capture generated IDs and starting counts.
- [ ] Convert logical import/reconciliation scenarios to the delivered actual workbook/table/schema contracts. Do not upload the logical scenario CSV as if it were a guaranteed supported file format.
- [ ] Save prior app/flow versions and document rollback plus data/file/approval cleanup. Safe failure injection and raw backend testing must use approved company tooling in development.
- [ ] Copy RESULT-LOG.csv/DEFECT-LOG.csv into company-controlled working storage; use fresh fixture run prefixes for destructive sessions.

Completion: each available prerequisite has evidence; unavailable items are named blockers against affected case IDs. The owner can run ready functional cases while other prerequisites remain pending.
