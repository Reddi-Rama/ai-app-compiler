def design_system(intent_data):
    
    app_type = intent_data.get("app_type", "Application")

    features = intent_data.get("features", [])

    architecture = {

        "app_name": app_type,

        "frontend": {
            "framework": "React",
            "pages": []
        },

        "backend": {
            "framework": "FastAPI",
            "modules": []
        },

        "database": {
            "type": "PostgreSQL",
            "tables": []
        },

        "authentication": True
    }

    # Generate pages/modules/tables from features

    for feature in features:

        architecture["frontend"]["pages"].append(
            feature
        )

        architecture["backend"]["modules"].append(
            feature
        )

        architecture["database"]["tables"].append(
            feature
        )

    return architecture