from pipeline.intent_extractor import extract_intent
from pipeline.architect import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair_engine import repair_schema

prompt = """
Build a CRM with:
- login
- contacts
- payments
- analytics dashboard
"""

intent = extract_intent(prompt)

architecture = design_system(intent)

schema = generate_schema(architecture)

validation = validate_schema(schema)

print("VALIDATION:")
print(validation)

if not validation["valid"]:

    repaired = repair_schema(
        schema,
        validation["errors"]
    )

    print("\nREPAIRED SCHEMA:")
    print(repaired)

else:
    print("\nSchema already valid.")