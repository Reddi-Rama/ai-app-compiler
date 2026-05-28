from pipeline.intent_extractor import extract_intent

prompt = """
Build a CRM with:
- login
- contacts
- payments
- analytics dashboard
"""

result = extract_intent(prompt)

print(result)