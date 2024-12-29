l = [
    "Axolotl",
    "Wombat",
    "Tuatara",
    "Kestrel",
    "Tapir",
    "Gerenuk",
    "Secretary Bird",
    "Coati",
    "Civet Cat",
    "Harpy Eagle",
    "Dumbo Octopus",
    "Shoebill Stork",
    "Leafy Sea Dragon",
    "Arapaima",
    "Quokka",
    "Pangasius Fish",
    "Horseshoe Crab",
    "Velvet Worm",
    "Antlion",
    "Nightjar",
    "Saiga Antelope",
    "Basking Shark",
    "Blobfish",
    "Glass Frog",
    "Aye-Aye",
    "Dragon Tree",
    "Taro ",
    "Rafflesia (Corpse Flower)",
    "Golden Barrel Cactus",
    "Japanese Maple",
    "Creeping Fig",
    "Bottlebrush Plant",
    "Crocus",
    "Juniper",
    "Olive Tree",
    "Secretary Bird",
    "Gerenuk",
    "Coati",
    "Tuatara",
    "Kestrel",
    "Tapir",
    "Civet Cat",
    "Kiwi(fruit)",
    "Harpy Eagle",
    "Pangasius Fish",
]

"""(Colocasia other varieties not mentioned)"""
import json

with open("bn.json", "r") as f:
    d = json.load(f)

l2 = d.keys()

for i in l:
    if i.lower() not in map(str.lower, l2):
        print(i)
