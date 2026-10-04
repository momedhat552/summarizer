![Tests](https://github.com/momedhat552/summarizer/actions/workflows/test.yml/badge.svg)
# Summarizer

A command-line tool that summarizes text using Google's Gemini API. It accepts text typed directly or a path to a text file, and you can choose how many sentences you want.

## Setup

1. Install the dependencies:

        pip install google-genai python-dotenv

2. Get a free API key from Google AI Studio (aistudio.google.com).

3. Create a file named `.env` in the project folder containing:

        GEMINI_API_KEY=your_key_here

## Usage

Summarize text typed in the command:

    py summarizer.py "your text here"

Summarize a text file:

    py summarizer.py notes.txt

Choose how many sentences (default is 2):

    py summarizer.py notes.txt 3

General form:

    py summarizer.py <text or filename> [sentences]

## Notes

- If the script reports that the model isn't found, model names change often. Update the `model=` line in `summarizer.py` to a current one. `list_models.py` prints the models available to your key.
- If you get a 503 error, the model is busy. Wait a minute and try again.
- Your `.env` file is listed in `.gitignore`, so your

