import json

with open("Jsons\\races.json", encoding="utf8") as test:  #open races.json as test
    race = json.load(test)


print(race["Dwarf"])
for k,v in race["Dwarf"].items():
    print("Key: " + k)
    print("Value: " + str(v))
