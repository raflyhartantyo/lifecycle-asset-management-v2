# Return Master Asset — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | (scope entry) | dataset, table |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | Compose |  |
| /properties/definition/actions/Compose | Compose | Compose | - | - | Get_items |  |
