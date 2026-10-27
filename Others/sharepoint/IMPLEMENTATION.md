# SharePoint setup and data contracts

18 schema Markdown files and 18 anonymized sample CSVs are supplied; 96 sample rows total. CSV header sets match their paired schemas. Historical full-export counts in documentation are not sample counts.

1. Inventory actual target lists, internal/display column names, types, required fields, choice sets, lookup/relationship rules, indexes, uniqueness and permissions.
2. Complete COLUMN-CONTRACT.csv from verified company-side metadata. All blank/unknown fields remain unresolved; infer neither storage types nor GUID-to-list mappings from field names alone.
3. Resolve whether Entity names the existing Organization_ID or a separate physical column. Define Function_ID, parent organization constraints and tuple-scoped authorization before V2 migration.
4. Verify Master_Asset2's purpose. It duplicates the packaged Master_Asset schema/sample but its runtime binding is not established by that fact.
5. Keep the disposal-request list outside target V2 provisioning; retain evidence from the legacy screen. Scope of any shared resources requires dependency review before removal.
6. Use anonymized sample copies only for controlled development tests. Backfill production only in a separately delivered migration with before/after counts, owner-approved mapping and rollback.

Backend permission enforcement is an open design item: UI menu checks and client-side filters alone do not demonstrate IT/CRESS isolation.
