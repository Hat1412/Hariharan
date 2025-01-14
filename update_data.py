import json

with open("final_data.json", "r") as f:
    d = json.load(f)

with open("K.json", "r") as f:
    d2 = json.load(f)

new_d = {
    "Legge's hawk-eagle": "Nisaetus kelaarti",
    "Wallace's hawk-eagle": "Nisaetus nanus",
    "Mountain hawk-eagle": "Nisaetus nipalensis",
    "Blyth's hawk-eagle": "Nisaetus alboniger",
    "Javan hawk-eagle": "Nisaetus bartelsi",
    "Sulawesi hawk-eagle": "Nisaetus lanceolatus",
    "Pinsker's hawk-eagle": "Nisaetus pinskeri",
    "Philippine hawk-eagle": "Nisaetus philippensis",
    "Changeable hawk-eagle": "Nisaetus cirrhatus",
    "Montagu's harrier": "Circus pygargus",
    "Hen harrier": "Circus cyaneus",
    "Northern harrier": "Circus hudsonius",
    "Western marsh harrier": "Circus aeruginosus",
    "Eastern marsh harrier": "Circus spilonotus",
    "African marsh harrier": "Circus ranivorus",
    "Swamp harrier": "Circus approximans",
    "Papuan harrier": "Circus spilothorax",
    "Malagasy harrier": "Circus macrosceles",
    "Réunion harrier": "Circus maillardi",
    "Long-winged harrier": "Circus buffoni",
    "Spotted harrier": "Circus assimilis",
    "Black harrier": "Circus maurus",
    "Cinereous harrier": "Circus cinereus",
    "Pallid harrier": "Circus macrourus",
    "Pied harrier": "Circus melanoleucos",
}

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
