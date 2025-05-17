# Import custom modules for text extraction and summarization
from text_extractor import extract_text_from_url, extract_text_from_file
from summarizer import summarize_text

# Import os module for file and path operations
import os

# Function to save the summary text to a file
def save_summary(summary, output_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the summary to the specified file with UTF-8 encoding
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)

# Main function to run the summarization process
def main():
    # Ask user whether they want to summarize text from a URL or a file
    input_type = input("Enter 'url' or 'file': ").strip().lower()
    
    if input_type == 'url':
        # If URL, prompt for the URL and extract text from it
        url = input("Enter URL: ").strip()
        text = extract_text_from_url(url)
        # Generate output filename based on the last part of the URL
        output_file = f"output/summary_url_{url.split('/')[-1]}.txt"
    
    elif input_type == 'file':
        # If file, prompt for the file path and extract text from it
        file_path = input("Enter file path: ").strip()
        text = extract_text_from_file(file_path)
        # Generate output filename based on the file's name
        output_file = f"output/summary_{os.path.basename(file_path)}"
    
    else:
        # Handle invalid input types
        print("Invalid input type.")
        return

    # Check if the extraction returned an error
    if "Error" in text:
        print(text)
        return

    # Generate a summary using the extracted text
    summary = summarize_text(text)

    # Print the summary to the console
    print("\nSummary:\n", summary)

    # Save the summary to the output file
    save_summary(summary, output_file)

    # Notify the user of the saved location
    print(f"Summary saved to {output_file}")

# Entry point of the script
if __name__ == "__main__":
    main()
