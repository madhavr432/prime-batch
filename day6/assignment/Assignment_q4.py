import json

with open("cities.json", "r") as f:
    data = json.load(f)
    print("Before:", data)

data["London"] = "9304000"

with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("After:", data)
