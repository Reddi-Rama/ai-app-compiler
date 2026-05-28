def repair_schema(schema, errors):
    
    repaired = schema.copy()

    for error in errors:

        # Missing top-level schemas
        if "Missing key: ui_schema" in error:

            repaired["ui_schema"] = {
                "pages": []
            }

        if "Missing key: api_schema" in error:

            repaired["api_schema"] = {
                "endpoints": []
            }

        if "Missing key: db_schema" in error:

            repaired["db_schema"] = {
                "tables": []
            }

        if "Missing key: auth_rules" in error:

            repaired["auth_rules"] = {
                "roles": ["admin", "user"]
            }

        # Fix malformed API endpoints
        if "API endpoint missing method" in error:

            for endpoint in repaired.get(
                "api_schema",
                {}
            ).get("endpoints", []):

                if "method" not in endpoint:

                    endpoint["method"] = "GET"

        # Fix malformed DB tables
        if "missing columns" in error:

            for table in repaired.get(
                "db_schema",
                {}
            ).get("tables", []):

                if "columns" not in table:

                    table["columns"] = [
                        "id",
                        "created_at"
                    ]

    return repaired