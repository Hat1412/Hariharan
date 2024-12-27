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
        print(response.choices[0].message.content)


def load_json_file(json_path):
    """Load and parse the content of a JSON file."""
    with open(json_path, "r") as file:
        data = json.load(file)
    return json.dumps(data, indent=2)


context = load_json_file("final_data.json")
question = "What is the purpose of the data in the JSON file?"
predict(
    f"""I have the following JSON data:{context}. Please answer the question: {question}"""
)

# l = [
# "Dog",	,"Cow"	,"Cat"	,"Horse","Donkey",	,"Tiger"	,"Lion"	,"Panther","Leopard",	,"Cheetah"	,"Bear"	,"Elephant","Polar bear",	,"Turtle"	,"Tortoise"	,"Crocodile",
# "Rabbit",	,"Porcupine"	,"Hare"	,"Hen","Pigeon",	,"Albatross"	,"Crow"	,"Fish","Dolphin",	,"Frog"	,"Whale"	,"Alligator",
# "Eagle",	"Flying","squirrel"	,"Ostrich"	,"Fox",
# "Goat",	,"Jackal"	,"Emu"	,"Armadillo",
# "Eel",	"Goose",	,"Arctic" ,"fox"	,"Wolf",
# "Beagle",	,"Gorilla"	,"Chimpanzee"	,"Monkey",
# "Beaver",	,"Orangutan"	,"Antelope"	,"Bat",
# "Badger",	"Giraffe", "Hermit","Crab"	,"Giant" ,"Panda",
# "Hamster",	"Cobra",	,"Hammerhead" ,"shark"	,"Camel",
# "Hawk",	,"Deer"	,"Chameleon"	,"Hippopotamus",
# "Jaguar"	"Chihuahua",	,"King" ,"Cobra"	,"Ibex",
# "Lizard",	,"Koala"	,"Kangaroo"	,"Iguana",
# "Llama",	,"Chinchillas"	,"Dodo"	,"Jellyfish",
# "Rhinoceros",	,"Hedgehog"	,"Zebra"	,"Possum",
# "Wombat",	,"Bison"	,"Bull"	,"Buffalo",
# "Sheep",	,"Meerkat"	,"Mouse"	,"Otter",
# "Sloth",	,"Owl"	,"Vulture"	,"Flamingo",
# "Racoon",	,"Mole"	,"Duck"	,"Swan",
# "Lynx"	"Monitor","lizard"	,"Elk"	,"Boar",
# "Lemur",	,"Mule"	,"Baboon"	,"Mammoth",
# "Blue whale",	"Rat"	,"Snake"	,"Peacock",
# ]


# predict(f"Give me only the scientific name of {i}")
