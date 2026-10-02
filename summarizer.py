import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

if len(sys.argv) < 2:
    print('Usage: py summarizer.py "text or filename" [sentences]')
    sys.exit(1)

arg = sys.argv[1]

if os.path.isfile(arg):
    with open(arg, encoding="utf-8") as f:
        text = f.read()


if len(sys.argv) > 2:
    sentences = sys.argv[2]
else: 
    sentences = "2"

try:
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=f"Summarize this in {sentences} sentences:\n\n{text}",
    )
    print(response.text)
except Exception as e:
    print(f"Something went wrong: {e}")