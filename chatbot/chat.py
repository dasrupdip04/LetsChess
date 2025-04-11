from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)
response= client.models.generate_content(
    model="gemini-1.5-flash",
    contents="What is life",
    
)
print(response.text)