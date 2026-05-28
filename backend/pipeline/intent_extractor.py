import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an AI intent extraction engine.

Return ONLY valid JSON.

Do NOT explain anything.
Do NOT add markdown.
Do NOT add headings.
Do NOT add code blocks.

Output format:

{
  "app_type": "string",
  "features": ["feature1", "feature2"]
}
"""

def extract_intent(user_prompt):

    completion = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Extract app intent from: {user_prompt}"
            }
        ],

        temperature=0
    )

    text = completion.choices[0].message.content.strip()

    start = text.find("{")
    end = text.rfind("}") + 1

    text = text[start:end]

    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e),
            "raw_output": text
        }