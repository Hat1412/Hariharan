import json

l = [
    "Hippo ",
    "Rhino",
    "Cockroach ",
    "Zebra",
    "Giraffe ",
    "Beetle ",
    "Beetle ",
    "Bed bug",
    "Caterpillar ",
    "Mosquito",
    "Housefly ",
    "Snail",
    "Bee",
    "Bumblebee ",
    "Scorpion ",
    "Crab",
    "Lobster",
    "Alligator ",
    "Tortoise",
    "Turtle ",
    "Monkey ",
    "Gorilla",
    "Boar",
    "Bison ",
    "Hog",
    "Cheetah ",
    "Leapord ",
    "Jaguar",
    "Panther ",
    "Tiger",
    "Lion",
    "Lioness ",
    "Puma ",
    "Orangutan ",
    "Chimpanzee ",
    "Dog ",
    "Cat",
    "Parrot",
    "Peagion",
    "Peacock",
    "Hen ",
    "Rooster",
    "Chicken ",
    "Crane",
    "Duck",
    "Goose",
    "Swan",
    "Peahen",
    "Crow",
    "Coocoo",
    "Owl",
    "Dragonfly",
    "Fox",
    "Snow leapord ",
    "Bear",
    "Polar bear",
    "Walrus",
    "Fish",
    "Penguin",
    "Sea lion",
    "Horse",
    "Snake",
    "Boa",
    "Hyena ",
    "Jackal",
    "Wolf",
    "Kite",
    "Eagle",
    "Vulture",
    "Lamb",
    "Sheep",
    "Goat",
    "Cow",
    "Octopus",
    "Whale",
    "Shark",
    "Tiger shark",
    "Kangaroo",
    "Koala",
    "llama",
]


with open("final_data.json", "r") as f:
    d = json.load(f)

cnl = [i["cn"] for i in d]
for i in l:
    if i.lower() not in [ele.lower() for ele in cnl]:
        print(i)



"""Cockroach
Beetle
Bed bug
Caterpillar
Housefly
Bee
Bumblebee

Scorpion
Lobster

Alligator
Mountain Goat

Turtle
Monkey
Bison
Hog
Cheetah
Puma
Orangutan
Chimpanzee
Parrot
Hen
Rooster
Chicken
Duck
Peahen
Coocoo
Snow leapord
Penguin
Sea lion
Boa
Hyena
Kite
Lamb
Shark"""