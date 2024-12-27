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


with open(r"D:\ACHU\Web\Hariharan\New folder\to_update.json", "r") as f:
    d = json.load(f)

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
# for i in l:
#     if i not in  
print(d)

for i in d.keys():
    predict(f"Give me only the scientific name of {i}")


