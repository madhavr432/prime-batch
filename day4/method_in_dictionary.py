info = {
    "name" : "madhav",
    "cgpa" : 9.2,
    "subject" : ["maths", "science"],
    "Score" : 97
}
print(info.keys())
print(info.values())
print(info.items())
print(info.get("cgpa"))
print(info.get("cgp"))
info.update({
    "state": "bihar"
})
print(info)
