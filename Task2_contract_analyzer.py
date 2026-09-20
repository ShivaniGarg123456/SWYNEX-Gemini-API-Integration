from google import genai

# Connect to Gemini using the environment variable
client = genai.Client()

# Sample contract for Task 2 demonstration
contract_text = """
FREELANCE SERVICE AGREEMENT

Payment:
The client shall pay the freelancer INR 25,000 within 15 days
of receiving the final deliverables.

Termination:
Either party may terminate this agreement by providing 30 days
written notice.

Intellectual Property:
All final work created by the freelancer and paid for by the client
shall belong to the client.

Confidentiality:
Both parties agree to keep confidential information private
and shall not disclose it to third parties.

Liability:
The agreement does not clearly specify a limitation of liability.
"""

prompt = f"""
You are an AI Legal Contract Compliance Auditor.

Analyze the following contract.

Check these important categories:
1. Payment
2. Termination
3. Intellectual Property
4. Confidentiality
5. Liability

For each category, provide:
- Status: Present, Missing, or Unclear
- Short explanation

Do not give legal advice or determine whether the contract is legally
valid or enforceable.

Contract:
{contract_text}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("========== CONTRACT AUDIT ==========")
print(response.text)