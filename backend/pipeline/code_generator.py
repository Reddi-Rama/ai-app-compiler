
def generate_code(architecture):

    frontend_pages = architecture.get(
        "frontend",
        {}
    ).get(
        "pages",
        []
    )

    backend_modules = architecture.get(
        "backend",
        {}
    ).get(
        "modules",
        []
    )

    frontend_code = {}

    for page in frontend_pages:

        component_name = (
            page.title()
            .replace(" ", "")
            + "Page"
        )

        frontend_code[page] = f'''
import React from "react"

function {component_name}() {{

    return (

        <div>

            <h1>{page} Page</h1>

        </div>

    )
}}

export default {component_name}
'''

    backend_code = {}

    for module in backend_modules:

        route_name = (
            module.lower()
            .replace(" ", "_")
        )

        backend_code[module] = f'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/{route_name}")
def get_{route_name}():

    return {{
        "message": "{module} endpoint working"
    }}
'''

    return {
        "frontend_code": frontend_code,
        "backend_code": backend_code
    }

