words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict= {}
for i in words:
    dict.update({i: len(i)})
print(dict)