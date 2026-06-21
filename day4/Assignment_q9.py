lst = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 1]

seen = set()
duplicates = set()

for item in lst:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("Duplicate elements:", duplicates)
