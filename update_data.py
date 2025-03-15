import json

with open("final_data.json", "r") as f:
    d = json.load(f)

with open("K.json", "r") as f:
    d2 = json.load(f)

new_d = {}

# for i in d2:
#     new_d[i["common_name"]] = i["binomial_nomenclature"]

cnl = [i["cn"] for i in d]

print(type(d))

for i, j in new_d.items():
    if i.lower() not in [ele.lower() for ele in cnl]:
        d.append(
            {
                "id": len(d),
                "cn": i,
                "Genus": j.split(" ")[0],
                "Species": j.split(" ")[1:],
                "bn": j,
            }
        )

with open("final_data.json", "w") as f:
    json.dump(d, f)
