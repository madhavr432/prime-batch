import json
py_obj1 = {
    "name": "madhav",
    "isStudent": True
}
# json_str1 = json.dumps(py_obj1)
# json_str = '{"name": "Madhav", "isStudent": true}'
# print(type(json_str))
# py_obj = json.loads(json_str)
# print(type(py_obj), py_obj)
# print(type(json_str1), json_str1)
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)
with open("data1.json", "w") as f:
    json.dump(py_obj1, f, indent = 4, sort_keys =True)