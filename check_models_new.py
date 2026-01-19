from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Listing models with google-genai SDK:")
try:
    for model in client.models.list():
        # print(model) # Too verbose
        print(model.name)
except Exception as e:
    print(f"Error: {e}")
