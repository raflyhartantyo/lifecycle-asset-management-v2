# Logical synthetic fixtures

These are scenario specifications, not import-ready SharePoint/Excel packages. Current target column types/internal names and import workbook contracts remain unverified. Complete FIELD-MAPPING.csv and bind symbolic identities before creating controlled development data. Use a UAT prefix/run ID and retain generated real record IDs in a private company-side register.

SCOPES defines two entities and three functions. ASSETS contains seven active records: five in A/A1, one in A/A2 and one in B/B1. INACTIVE-ASSETS contains A008 only. Within A/A1: Available A001/A003/A007 (3); In Use A002/A004 (2). BO_A owns A001/A002/A005/A007; BO_B owns A003/A004/A006. INVENTORY starts I001=10, I002=0. A three-unit transfer should leave source=7 and destination=3, with total=10.

IMPORT-SCENARIOS describes four logical rows: valid R1, invalid R2, duplicate R3 and valid-but-unselected R4. Convert to the delivered import contract, supplying all other required fields; to isolate partial-import tests, select R1 only. Expected creates=1 and original A001 unchanged. Duplicate matching keys are an architecture dependency; do not mark the duplicate case passed before that contract is fixed.

RECONCILIATION-SCENARIOS gives matched A001=700, A002 ledger=900 versus register=1000 (difference 100), an unknown ledger code, and disposed A008. Omit A003 from the ledger for a register-only case. Adapt accounting field/group definitions to the validated target contract; these figures are test data, not accounting policy.

Create an open stock cycle with A001/A002 assigned to RESP_A, a separate historical closed cycle with the same assigned work, and a replacement assignment for RESP_B when executing the reassignment case. Configure due-date default using the agreed company configuration; no fixed duration is assumed. Approved notification destinations must be controlled test mailboxes/Teams locations. Symbolic aliases are not email addresses and must not be used as real recipients.

Reset mutated fixtures between destructive/movement sessions; never load these into production. Preserve disposed/history/audit evidence and use approved development cleanup. Source fixtures are unchanged; results/actual IDs remain company-side.
