# Flow index

Display name to source folder GUID. Folders are named by display name in this package.

| Display name | Original GUID |
|---|---|
| SO_Respondents_Confirm | 0eefb3df-e0fc-4040-aa49-6f2a56a7a2c2 |
| InTune Flow | 17f8b7bb-68a9-4421-9cfc-7a5559061408 |
| Accounting Reconciliation - Approval Request | 1f8fcf93-8071-4149-aa5f-654cedf4e1ef |
| Flow Networking Device | 23af3065-df1a-48af-bfae-69c1071ad65a |
| SO_Respondent_Save | 2cf2b4d9-0683-4986-b2c8-67e2f1939e60 |
| Accounting_ReconsiliationV2 | 3fbd7c1e-d225-43e3-b94f-8aef8bca72e7 |
| Bulk_Registration | 454540b3-7dfa-44dc-8e88-1a4598783d03 |
| Export Data | 587369ae-b9c6-40b5-a982-9aec8d3b37d4 |
| PowerAppV2 -> Respond to a Power App or flow | 5e948931-5ff7-4537-9a9b-27ffa17b2b7d |
| Stock_Opname_In_Use_Trigger | 939219c2-b08e-46cc-8981-1968b7550384 |
| Data Refresh ALM | 97120110-ff02-49ce-b23f-53234a5a1d60 |
| Accounting_ReconsiliationV3 | 9ba319fb-eb8f-49d1-9310-fbfd296b567b |
| Stock_Opname_Available_Trigger | 9d97ebfb-7d3e-4017-9bf9-d212f02f55b8 |
| Return Master Asset | d56caa4a-29ce-4b51-ae47-87f4367f26a7 |
| Stock_Opname_In_Use_Match | ed89ad96-a2e9-41e4-b2b4-79b7629d9d9b |

## Placeholders to set on import
- `<REQUESTER-EMAIL>`: the requester and CC address in `SO_Respondents_Confirm` and `Stock_Opname_In_Use_Trigger`. Set to the owning team's address in the target environment.
- `<REDACTED-ID>`: Power BI report and tenant IDs (dashboard and flow definitions). Set the target environment's values.
- `C:\Users\<user>`: local paths in the docs only.
