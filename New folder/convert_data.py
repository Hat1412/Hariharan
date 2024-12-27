import json

source = "bn.json"
dest1 = "final_data.json"

with open(source, "r") as f:
    d1 = json.load(f)

with open(dest1, "r") as f:
    l = json.load(f)



def update_new_data(counter = 2):
    new_data = {}
    new_data = {k: v for k, v in new_data.items() if k not in d1}
    if counter == 1:
        print(new_data)
    if counter == 2:
        d1.update(new_data)


def update_final_dest():
    l = []
    for index, i in enumerate(d1.items()):
        genus = i[1].split(" ")[0]
        species = i[1].split(" ")[1:]
        species = " ".join(species)

        l.append(
            {
                "id": index + 1,
                "cn": i[0],
                "Genus": genus,
                "Species": species,
                "bn": i[1],
            }
        )

    with open("final_data.json", "w") as f:
        json.dump(l, f)

if __name__ == "__main__":
    # update_new_data(1)
    update_final_dest()