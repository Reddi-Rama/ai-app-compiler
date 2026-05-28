from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

from pipeline.retry_engine import retry_operation
import json

from pipeline.ambiguity_handler import detect_ambiguity
from pipeline.intent_extractor import extract_intent
from pipeline.architect import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema
from pipeline.consistency_checker import check_consistency
from pipeline.runtime_simulator import simulate_runtime
from pipeline.code_generator import generate_code


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {
        "message": "AI App Compiler Backend Running"
    }


@app.get("/evaluation-report")
def get_evaluation_report():

    with open(
        "evaluation/evaluation_report.json",
        "r"
    ) as f:

        report = json.load(f)

    return report


@app.post("/generate-app")
def generate_app(req: PromptRequest):

    # Ambiguity Detection
    ambiguity = detect_ambiguity(req.prompt)

    if ambiguity["clarification_needed"]:

        return {
            "status": "clarification_required",
            "details": ambiguity
        }

    # Stage 1
    intent = retry_operation(
        lambda: extract_intent(req.prompt)
    )

    # Stage 2
    architecture = retry_operation(
        lambda: design_system(intent)
    )

    # Stage 3
    schema = retry_operation(
        lambda: generate_schema(architecture)
    )

    # Stage 4
    validation = validate_schema(schema)

    # Stage 5
    repaired_schema = schema

    if not validation["valid"]:

        repaired_schema = repair_schema(
            schema,
            validation["errors"]
        )

    # Stage 6
    consistency = check_consistency(
        repaired_schema
    )

    # Stage 7
    runtime = simulate_runtime(
        repaired_schema
    )

    # Stage 8
    generated_code = generate_code(
        architecture
    )

    return {
        "intent": intent,
        "architecture": architecture,
        "schema": repaired_schema,
        "validation": validation,
        "consistency": consistency,
        "runtime": runtime,
        "generated_code": generated_code
    }