import json
from ollama import Ollama


def read_json(file_path):
    """Reads a JSON file and returns its content."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return None


def chat_with_ollama(prompt, model="default_model"):
    """Sends a prompt to the Ollama chatbot and returns the response."""
    try:
        ollama_client = Ollama()
        response = ollama_client.chat(model=model, prompt=prompt)
        return response.get("response", "No response returned.")
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
# File path to the JSON file containing queries
    response = chat_with_ollama(query)
    if response:
        print(f"Response: {response}\n")


if __name__ == "__main__":
    main()
