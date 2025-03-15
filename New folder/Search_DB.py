l = [

]

import json

with open("bn.json", "r") as f:
    d = json.load(f)

l2 = d.keys()

for i in l:
    if i.lower() not in map(str.lower, l2):
        print(i)
