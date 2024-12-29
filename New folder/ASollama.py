import aisuite as ai
import json

client = ai.Client()

models = ["ollama:llama3.2"]


def predict(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    for model in models:
        response = client.chat.completions.create(
            model=model, messages=messages, temperature=0.75
        )
        return response.choices[0].message.content


def load_json_file(json_path):
    """Load and parse the content of a JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return json.dumps(data, indent=2)


context = load_json_file(r"D:\ACHU\New folder\Hariharan\New folder\K.json")
question = "Give me the data of all organisms with even ids?"

predict(
    f"""I have the following JSON data:{context}. Please answer the question: {question}"""
)
