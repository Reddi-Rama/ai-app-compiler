from pipeline.intent_extractor import extract_intent
from pipeline.architect import design_system

prompt = """
Build a CRM with:
- login
- contacts
- payments
- analytics dashboard
"""

intent = extract_intent(prompt)

architecture = design_system(intent)

print(architecture)