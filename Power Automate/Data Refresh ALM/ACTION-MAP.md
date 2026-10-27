# Data Refresh ALM — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Refresh_a_dataset | Refresh_a_dataset | OpenApiConnection | shared_powerbi | RefreshDataset | (scope entry) | datasetid, groupid |
