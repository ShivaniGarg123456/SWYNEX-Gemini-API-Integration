from google import genai

# Connect to Gemini using the API key stored in the environment variable
client = genai.Client()

# Example contract clause
contract_text = """
Either party may terminate this agreement by giving 30 days written notice.
"""

# Ask Gemini to analyze the clause
prompt = f"""
You are an AI Legal Contract Compliance Auditor.

Analyze the following contract text.

Identify:
1. Clause type
2. Whether the clause is present
3. A short explanation

Contract text:
{contract_text}

Return the answer in a simple format.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)