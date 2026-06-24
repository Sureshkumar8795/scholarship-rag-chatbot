import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv("config.env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are an AI Scholarship Assistant.

Use ONLY the provided context.

If information is not available,
say:
"Information not found in the knowledge base."

Context:
{context}

Question:
{question}

Provide a clear, student-friendly answer.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content