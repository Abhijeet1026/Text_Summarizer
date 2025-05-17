# Import necessary modules
import anthropic  # Anthropic Python SDK for interacting with Claude models
import os         # For accessing environment variables like the API key

# Initialize the Anthropic client using an API key stored in an environment variable
client = anthropic.Anthropic(api_key=os.getenv('my_key_gen'))

# Print the client object to confirm it was created (optional debug step)
print(client)

# Function to create a structured prompt for summarization
def create_summary_prompt(text):
    return f"""You are a highly skilled summarizer. Summarize the following text in 100–200 words, 
capturing the main ideas and key details in a concise, coherent, and neutral tone. 
Focus on clarity and avoid unnecessary elaboration. Exclude any external opinions or assumptions. 
Text:
{text}"""

# Function to summarize text using the Claude model
def summarize_text(text, max_tokens=300):
    # Return an error if the input text is too short or empty
    if not text or len(text.strip()) < 50:
        return "Text is too short or empty."
    
    try:
        # Make a request to the Claude API to generate a summary
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Specify the Claude model to use
            max_tokens=max_tokens,              # Set the token limit for the summary
            temperature=0.5,                     # Set creativity level (lower is more deterministic)
            messages=[
                {"role": "user", "content": create_summary_prompt(text)}  # Provide user prompt
            ]
        )
        
        # Extract the summary text from the response
        summary = response.content[0].text.strip()
        
        # Check if the summary is within the desired 100–200 word range
        word_count = len(summary.split())
        if 100 <= word_count <= 200:
            return summary
        
        # Return the summary even if it's outside the word limit, but with a note
        return f"Summary is {word_count} words, outside 100–200 range: {summary}"
    
    except anthropic.APIError as e:
        # Handle API errors gracefully
        return f"API error: {e}"
