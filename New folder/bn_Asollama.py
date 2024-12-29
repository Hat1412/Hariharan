from ollama import chat
from ollama import ChatResponse
import json


def load_json_file(json_path):
    """Load and parse the content of a JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return json.dumps(data, indent=2)


response: ChatResponse = chat(
    model="llama3.2",
    # temperature=0.5,
    messages=[
        {
            "role": "user",
            "content": f"With reference to the {load_json_file('final_data.json')}, what is given",
        },
    ],
)

print(response["message"]["content"])
