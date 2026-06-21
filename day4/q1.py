info = {
    ("Alice", "Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
}
s = set()
for name,courses in info:
    s.add(courses)
    if(courses=="English"):
        print(name)
print(s)
dict = {}
for name,courses in info:
    if(dict.get(name) == None ):
        dict.update({name: set()})
        dict[name].add(courses)
    else:
        dict[name].add(courses)
print(dict)