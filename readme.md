# 📄 Text Summarization Tool using Anthropic Claude

This project extracts large bodies of text from either a webpage or a local file, summarizes the text using Anthropic's Claude model (Claude 3.5 Sonnet), and saves the summary in a local output directory.

---

## ✅ Features

- Extracts text from web pages or local `.txt` files.
- Automatically skips noise (scripts, styles, navbars, etc.).
- Begins parsing from `"CHAPTER I"` to focus on meaningful narrative content.
- Summarizes long text into 100–200 words with a clear, neutral tone using Claude API.
- Handles errors like bad URLs, missing files, and API issues.
- Saves the summary in a structured `output/` folder.

---

## 🛠️ Setup Instructions

### Step 1: Create a virtual environment
```python3.10 -m venv env``` 

### Step 2: Activate the virtual environment
```source env/bin/activate```

To deactivate the virtual environment when you're done:
```deactivate```

### Step 3: Install dependencies
```pip install -r requirements.txt```

If requirements.txt doesn't exist, install manually:
```pip install requests beautifulsoup4 anthropic```

Then save dependencies:
```pip freeze > requirements.txt```

#### Step 4: Add your Anthropic API Key
Create an API key from the Anthropic Console and export it as an environment variable:
```export my_key_gen='your_api_key'```



## 🧠 Code Overview
### text_extractor.py

- Downloads and parses HTML content.

- Removes unwanted tags (<script>, <style>, <nav>, etc.).

- Starts text from "CHAPTER I" if present.

- Returns the first 10,000 characters of cleaned text.

- extract_text_from_file(file_path)

- Reads local .txt files.

- Cleans up spacing and formatting.

- Returns the first 10,000 words.

### summarizer.py

- create_summary_prompt(text)

- Prepares a structured prompt instructing Claude to summarize in 100–200 words.

- summarize_text(text, max_tokens=300)

- Sends the prompt to Claude using the anthropic Python SDK.

- Returns the generated summary.

- Warns if the summary is outside the expected word range.

### main.py

- Asks the user for input type: url or file.

- Extracts text using the relevant method.

- Calls summarize_text to generate a summary.

- Prints and saves the result to the output/ folder.

- save_summary(summary, output_path)

- Automatically creates the output/ directory (if not present).

- Writes the summary to a .txt file with a meaningful name.

📂 Project Structure

```
project/
│
├── text_extractor.py      # Extracts and cleans text
├── summarizer.py          # Summarizes text using Claude API
├── main.py                # Command-line interface
├── output/                # Folder where summaries are saved
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
## 💡 Future Enhancements

- Add PDF and DOCX support.

- Batch summarize multiple files.

- Web-based interface with upload and preview.

- Claude model selection via CLI flags.

- Dockerize the project for deployment.


