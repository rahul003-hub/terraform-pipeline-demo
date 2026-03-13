import json
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

with open("tfplan.json") as f:
    plan = f.read()

prompt = f"""
Analyze this Terraform plan and find:
1. Security issues
2. Misconfiguration
3. Cost risks
4. Best practice violations

Terraform Plan:
{plan}
"""

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.content[0].text)
