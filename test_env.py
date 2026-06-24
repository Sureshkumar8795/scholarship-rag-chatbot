import os
from dotenv import load_dotenv

load_dotenv("config.env")

print(os.getenv("GROQ_API_KEY"))