def check_consistency(schema):
    
    issues = []

    # -------------------------
    # UI ↔ API consistency
    # -------------------------

    ui_pages = []

    if "ui_schema" in schema:

        ui_pages = [
            page["name"]
            for page in schema["ui_schema"].get(
                "pages",
                []
            )
        ]

    api_routes = []

    if "api_schema" in schema:

        api_routes = [
            endpoint["route"]
            for endpoint in schema["api_schema"].get(
                "endpoints",
                []
            )
        ]

    for page in ui_pages:

        expected_route = f"/api/{page}"

        if expected_route not in api_routes:

            issues.append(
                f"Missing API for UI page: {page}"
            )

    # -------------------------
    # API ↔ DB consistency
    # -------------------------

    db_tables = []

    if "db_schema" in schema:

        db_tables = [
            table["name"]
            for table in schema["db_schema"].get(
                "tables",
                []
            )
        ]

    for route in api_routes:

        route_name = route.replace("/api/", "")

        if route_name not in db_tables:

            issues.append(
                f"No DB table for API route: {route}"
            )

    # -------------------------
    # Auth consistency
    # -------------------------

    if "login" in ui_pages:

        if "auth_rules" not in schema:

            issues.append(
                "Login page exists but auth_rules missing"
            )

    return {
        "consistent": len(issues) == 0,
        "issues": issues
    }