from pipeline.intent_extractor import extract_intent
from pipeline.architect import design_system
from pipeline.schema_generator import generate_schema

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

print(schema)