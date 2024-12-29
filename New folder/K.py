l = []

import json

with open("final_data.json", "r") as f:
    d = json.load(f)

l2 = [d[i]["cn"] for i in range(0, 666)]
l2.extend([d[i]["Genus"] for i in range(0, 666)])


for i in l:
    if i.lower() not in map(str.lower, l2):
        print(i)
