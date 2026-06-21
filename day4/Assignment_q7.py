str = input("Enter the string: ")
count = 0
for ch in str:
    if ch == ' ':
        count+=1
print(count)