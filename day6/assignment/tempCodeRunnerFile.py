import json

with open("cities.json", "r") as f:
    data = json.load(f)
    print(data)
data["London"]= "9304000"
with open("cities.json", "w") as f:
    json.load(f)
    f.write(data, f, indent = 4)