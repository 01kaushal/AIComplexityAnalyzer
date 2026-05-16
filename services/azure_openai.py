import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

SYSTEM_PROMPT = """
You are a senior Enterprise AI Transformation
and Business Complexity Analysis System.

Analyze enterprise applications and business workflows.

Generate:
1. AI Adoption Score
2. Business Complexity
3. Automation Maturity
4. Architecture Complexity
5. AI Dependency Level
6. Operational Risk
7. Scalability Readiness
8. Recommendations

Keep output professional and structured.
"""


def analyze_complexity(user_input):

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content