from google import generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the genai client
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")


# Terminal loop
print("🤖 GeminiGPT is online. Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        print("GeminiGPT: Bye!")
        break

    response = model.generate_content(prompt)
    print(f"GeminiGPT: {response.text}\n")
