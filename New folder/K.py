l = [
    "Dog",
    "Cow",
    "Cat",
    "Horse",
    "Donkey",
    "Tiger",
    "Lion",
    "Panther",
    "Leopard",
    "Cheetah",
    "Bear",
    "Elephant",
    "Polar bear",
    "Turtle",
    "Tortoise",
    "Crocodile",
    "Rabbit",
    "Porcupine",
    "Hare",
    "Hen",
    "Pigeon",
    "Albatross",
    "Crow",
    "Fish",
    "Dolphin",
    "Frog",
    "Whale",
    "Alligator",
    "Eagle",
    "Flying squirrel",
    "Ostrich",
    "Fox",
    "Goat",
    "Jackal",
    "Emu",
    "Armadillo",
    "Eel",
    "Goose",
    "Arctic fox",
    "Wolf",
    "Beagle",
    "Gorilla",
    "Chimpanzee",
    "Monkey",
    "Beaver",
    "Orangutan",
    "Antelope",
    "Bat",
    "Badger",
    "Giraffe",
    "Hermit Crab",
    "Giant Panda",
    "Hamster",
    "Cobra",
    "Hammerhead shark",
    "Camel",
    "Hawk",
    "Deer",
    "Chameleon",
    "Hippopotamus",
    "Jaguar",
    "Chihuahua",
    "King Cobra",
    "Ibex",
    "Lizard",
    "Koala",
    "Kangaroo",
    "Iguana",
    "Llama",
    "Chinchillas",
    "Dodo",
    "Jellyfish",
    "Rhinoceros",
    "Hedgehog",
    "Zebra",
    "Possum",
    "Wombat",
    "Bison",
    "Bull",
    "Buffalo",
    "Sheep",
    "Meerkat",
    "Mouse",
    "Otter",
    "Sloth",
    "Owl",
    "Vulture",
    "Flamingo",
    "Racoon",
    "Mole",
    "Duck",
    "Swan",
    "Lynx",
    "Monitor lizard",
    "Elk",
    "Boar",
    "Lemur",
    "Mule",
    "Baboon",
    "Mammoth",
    "Blue whale",
    "Rat",
    "Snake",
    "Peacock",
]

import json

with open("final_data.json", "r") as f:
    d = json.load(f)

l2 = [d[i]["cn"] for i in range(0, 666)]
l2.extend([d[i]["Genus"] for i in range(0, 666)])


for i in l:
    if i.lower() not in map(str.lower, l2):
        print(i)

"""
Leopard
Elephant
Polar bear
Turtle
Tortoise
Rabbit
Porcupine
Hare
Hen
Pigeon
Fish
Dolphin
Frog
Whale
Eagle
Flying squirrel
Eel
Goose
Beagle
Monkey
Orangutan
Badger
Giraffe
Hermit Crab
Giant Panda
Hamster
Cobra
Hammerhead shark
Camel
Hawk
Deer
Chameleon
Chihuahua
Lizard
Llama
Chinchillas
Dodo
Jellyfish
Hedgehog
Possum
Bull
Buffalo
Meerkat
Mouse
Sloth
Vulture
Flamingo
Racoon
Mole
Swan
Monitor lizard
Elk
Boar
Lemur
Mule
Mammoth
Rat
Snake
Peacock
"""
