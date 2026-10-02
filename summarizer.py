import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

if len(sys.argv) < 2:
    print('Usage: python summarize.py "your text here"')
    sys.exit(1)

text = sys.argv[1]

try:
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=f"Summarize this in 2 sentences:\n\n{text}",
    )
    print(response.text)
except Exception as e:
    print(f"Something went wrong: {e}")