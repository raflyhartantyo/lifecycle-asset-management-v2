# V2 SharePoint foundation — delivery 001

Status: manual creation guidance ready for the first two reference lists; implementation NOT RUN. This is a new V2 contract, not a reproduction of the untyped baseline schema. Operational data and access-control contracts are still being designed.

Start with [CREATION-GUIDE.md](CREATION-GUIDE.md). Exact fields/settings are in [FOUNDATION-COLUMNS.csv](FOUNDATION-COLUMNS.csv); future stages are in [CREATION-ORDER.md](CREATION-ORDER.md). These CSVs are documentation, not files to import as list data.

Scope: SITE-A; dedicated empty V2 lists named LAM2_Organizations and LAM2_Functions. Existing baseline lists remain untouched. Entity means Organization; no duplicate Entity column is introduced. A function belongs to exactly one organization (D002). Scope identifiers and reference relationships are not access grants.

Only approved site maintainers should write these reference lists during setup. Operational role assignments, task history, exports and data access will be implemented separately. Confirm permissions on the completed SITE-A before adding records or connecting the app. Creation of these lists alone does not enforce entity/function isolation.

Company observations: [ENVIRONMENT-FACTS.md](../../handover/ENVIRONMENT-FACTS.md).

## Application-controlled mandatory fields

D044 supersedes the original Required=Yes storage flags. FOUNDATION-COLUMNS.csv now separates SharePointRequired from BusinessRequired. Configure editable business fields as optional in SharePoint; the later application requires valid names/codes/parent organization. Keep the unique constraints, lookup relationship and indexes. Empty list creation does not implement any application validation; keep these lists empty until master-data entry is delivered.

## Operational architecture — design contract

The [operational data model](../../architecture/OPERATIONAL-DATA-MODEL.md) and [machine-readable field contract](OPERATIONAL-DATA-CONTRACT.json) now cover the proposed logical reference/register, operation/history, stock, reconciliation, approval, valuation and supporting records. These are architecture resources, not import/provisioning artifacts or a one-list-per-entity instruction. Only the original Organizations/Functions guide is currently creation-ready. D072 keeps connector/permission configuration with the owner at implementation time; no setup report is needed to continue design.
