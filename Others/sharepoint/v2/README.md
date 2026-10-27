# V2 SharePoint foundation — delivery 001

Status: manual creation guidance ready for the first two reference lists; implementation NOT RUN. This is a new V2 contract, not a reproduction of the untyped baseline schema. Operational data and access-control contracts are still being designed.

Start with [CREATION-GUIDE.md](CREATION-GUIDE.md). Exact fields/settings are in [FOUNDATION-COLUMNS.csv](FOUNDATION-COLUMNS.csv); future stages are in [CREATION-ORDER.md](CREATION-ORDER.md). These CSVs are documentation, not files to import as list data.

Scope: SITE-A; dedicated empty V2 lists named LAM2_Organizations and LAM2_Functions. Existing baseline lists remain untouched. Entity means Organization; no duplicate Entity column is introduced. A function belongs to exactly one organization (D002). Scope identifiers and reference relationships are not access grants.

Only approved site maintainers should write these reference lists during setup. Operational role assignments, task history, exports and data access will be implemented separately. Confirm permissions on the completed SITE-A before adding records or connecting the app. Creation of these lists alone does not enforce entity/function isolation.

Company observations: [ENVIRONMENT-FACTS.md](../../handover/ENVIRONMENT-FACTS.md).
