# Export Data — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Create_CSV_table | Create_CSV_table | Table | - | - | Initialize_variable |  |
| /properties/definition/actions/Create_file | Create_file | OpenApiConnection | shared_sharepointonline | CreateFile | Create_CSV_table | body, dataset, folderPath, name |
| /properties/definition/actions/Create_sharing_link_for_a_file_or_folder | Create_sharing_link_for_a_file_or_folder | OpenApiConnection | shared_sharepointonline | CreateSharingLink | Create_file | dataset, id, permission/scope, permission/type, table |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | Do_until |  |
| /properties/definition/actions/Do_until | Do_until | Until | - | - | Create_sharing_link_for_a_file_or_folder |  |
| /properties/definition/actions/Do_until/actions/Get_file_metadata_using_path | Get_file_metadata_using_path | OpenApiConnection | shared_sharepointonline | GetFileMetadataByPath | (scope entry) | dataset, path |
| /properties/definition/actions/Do_until/actions/Delay | Delay | Wait | - | - | Get_file_metadata_using_path |  |
| /properties/definition/actions/Do_until/actions/Set_variable | Set_variable | SetVariable | - | - | Get_file_metadata_using_path |  |
| /properties/definition/actions/Initialize_variable | Initialize_variable | InitializeVariable | - | - | (scope entry) |  |
