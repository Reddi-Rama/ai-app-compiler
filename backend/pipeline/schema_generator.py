def generate_schema(architecture):
    
    pages = architecture["frontend"]["pages"]

    schema = {

        "ui_schema": {
            "pages": []
        },

        "api_schema": {
            "endpoints": []
        },

        "db_schema": {
            "tables": []
        }
    }

    for page in pages:

        schema["ui_schema"]["pages"].append({
            "name": page,
            "components": [
                "header",
                "form",
                "button"
            ]
        })

        schema["api_schema"]["endpoints"].append({
            "route": f"/api/{page}",
            "method": "GET"
        })

        schema["db_schema"]["tables"].append({
            "name": page,
            "columns": [
                "id",
                "created_at"
            ]
        })

    return schema