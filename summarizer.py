import os
import sys
from dotenv import load_dotenv
from google import genai

def parse_sentence_count(value):
    if not value.isdigit():
        raise ValueError("The number of sentences must be a whole number, like 3.")
    return int(value)

def get_text(arg):

    if os.path.isfile(arg):
        with open(arg, encoding="utf-8") as f:
            return f.read()
    return arg






def main():

    load_dotenv()
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    if len(sys.argv) < 2:
        print('Usage: py summarizer.py "text or filename" [sentences]')
        sys.exit(1)


    text = get_text(sys.argv[1])

    sentences = 2

    if len(sys.argv) > 2:
        try:
            sentences = parse_sentence_count(sys.argv[2])
        except ValueError as e:
            print (e)
            sys.exit(1)
    
    

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=f"Summarize this in {sentences} sentences:\n\n{text}",
        )
        print(response.text)
    except Exception as e:
        print(f"Something went wrong: {e}")




if __name__ == "__main__":
    main()