import json
import aisuite as ai

client = ai.Client()
models = ["ollama:llama3.2"]

def load_json_file(json_path):
    """Load and parse the content of a JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return json.dumps(data, indent=2)


def ask_question_with_aisuite(context, question):
    """Ask a question using AISuite."""
    ai = AISuite(model="ollama:llama3.2")  # Use AISuite-compatible models
    prompt = f"""
    I have the following JSON data:
    {context}

    Please answer the question: {question}
    """
    response = ai.query(prompt)
    return response


# if __name__ == "__main__":
#     # Path to your JSON file
#     json_path = "your_file.json"  # Replace with the actual path to your JSON file

#     # Load the JSON file
#     json_data = load_json_file("final_data.json")

#     # Prepare context for the AI model
#     context = prepare_context(json_data)

#     # Define a question
#     question = "What is the purpose of the data in the JSON file?"

#     # Get the answer from AISuite
#     answer = ask_question_with_aisuite(context, question)
#     print(f"Answer: {answer}")

print(load_json_file("final_data.json"))
