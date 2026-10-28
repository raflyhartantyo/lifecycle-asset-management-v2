# reference-foundation-002 — list mapping and manual reference browser

Status: resources prepared for manual implementation; company configuration, Power Fx compilation and runtime tests NOT RUN. This is an incremental target resource package, not the completed production replacement. The original baseline source is unchanged.

## Scope

- Exact field/settings contract for LAM2_Categories, LAM2_AssetTypes and LAM2_Buildings, extending the original Organization/Function foundation.
- Three fixed Accounting Category seed rows; no invented Asset Types, Buildings or accounting mappings.
- Manual Studio control/property/formula resources for a read-only three-tab catalogue screen in the blank app, with context input, refresh/error behavior and brand tokens.
- Feature cases, source-level validator, implementation/rollback guidance and an optional concrete implementation Q&A prompt.

## Entry points

[Physical list guide](../../sharepoint/v2/reference-foundation-002/README.md) · [App package](../../../Power%20Apps/Lifecycle%20Asset%20Management%20V2/target-v2/reference-catalogues/README.md) · [Optional Q&A aid](../../prompts/PENDING-004-reference-catalogues.md).

The owner configures the SharePoint connector, source permissions and context adapter when implementing. No access questionnaire is requested. Direct reference reads are the adapter supplied here; the operational writer/backend design remains a separate responsibility. A UI context flag is not authentication or source security.

## Validation boundaries

Local checks cover file relationships, column/lookup settings expressed by the contract, exact seed values, control/property consistency, read-only formula resources and absence of baseline changes. These checks do not compile Power Fx, validate Studio's actual schema, prove delegation/security, or run a company flow. Run the package cases later and record actual evidence; keep unexecuted checks NOT RUN.

No Power Automate flow is required or supplied for this narrow read-only feature. No full .msapp, solution or YAML control package is represented as delivered. Maintenance writers, operational asset/inventory records, approvals and finance remain later feature implementations.

## Recovery

App rollback uses the saved pre-change app version/formulas and package-specific controls, checking later dependencies. SharePoint schema/data changes require their own corrective plan; restoring an app does not revert them. Preserve existing list consumers and history; never use destructive list cleanup as a default rollback.
