# Import necessary libraries
import requests  # For making HTTP requests to fetch webpage content
from bs4 import BeautifulSoup  # For parsing and extracting HTML content
import re  # For regular expressions and text cleaning

# Function to extract text from a given URL
def extract_text_from_url(url):
    try:
        # Send a GET request to the URL with a 10-second timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error if the response is not successful (e.g., 404)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted HTML elements like script, style, nav, etc.
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Extract all text from the HTML, separated by spaces, and strip leading/trailing whitespace
        text = soup.get_text(separator=' ', strip=True)

        # Normalize whitespace: collapse multiple spaces into one
        cleaned_text = ' '.join(text.split())
        
        # Start extracting text from "CHAPTER I" if it's found
        chapter_start = cleaned_text.find('CHAPTER I')
        if chapter_start != -1:
            cleaned_text = cleaned_text[chapter_start:]
        
        # Return the first 10,000 characters of the cleaned text
        return cleaned_text[:10000]
    
    except requests.RequestException as e:
        # Handle network or request-related errors
        return f"Error fetching URL: {e}"

# Uncomment to test the function with a Project Gutenberg book
# print(extract_text_from_url('https://www.gutenberg.org/cache/epub/56577/pg56577.txt'))

# Function to extract and clean text from a local text file
def extract_text_from_file(file_path):
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Replace multiple whitespace characters (including newlines) with a single space
            text = re.sub(r'\s+', ' ', text).strip()
         
            # Limit to the first 5000 words
            words = text.split()
            return ' '.join(words[:10000])
    
    except FileNotFoundError:
        # Handle file not found error
        return f"File not found: {file_path}"
    
    except Exception as e:
        # Handle any other exceptions
        return f"Error reading file: {e}"

# Uncomment to test the function with a local file
# print(extract_text_from_file('text_file.txt'))
