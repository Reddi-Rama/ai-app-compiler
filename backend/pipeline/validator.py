REQUIRED_KEYS = [
    "ui_schema",
    "api_schema",
    "db_schema",
    "auth_rules"
]

def validate_schema(schema):

    errors = []

    # Missing top-level keys
    for key in REQUIRED_KEYS:

        if key not in schema:
            errors.append(f"Missing key: {key}")

    # Validate UI pages
    if "ui_schema" in schema:

        pages = schema["ui_schema"].get("pages", [])

        if not isinstance(pages, list):
            errors.append("ui_schema.pages must be a list")

    # Validate API endpoints
    if "api_schema" in schema:

        endpoints = schema["api_schema"].get("endpoints", [])

        for endpoint in endpoints:

            if "route" not in endpoint:
                errors.append("API endpoint missing route")

            if "method" not in endpoint:
                errors.append("API endpoint missing method")

    # Validate DB schema
    if "db_schema" in schema:

        tables = schema["db_schema"].get("tables", [])

        for table in tables:

            if "name" not in table:
                errors.append("DB table missing name")

            if "columns" not in table:
                errors.append(
                    f"Table {table.get('name')} missing columns"
                )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }