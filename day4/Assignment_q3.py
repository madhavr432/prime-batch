list1 = []
list2 = []
n1 = int(input("How many elements? in list 1:  "))

for i in range(n1):
    elem = input("Enter element : ")
    list1.append(elem)
n2 = int(input("How many elements? in list 2:  "))

for i in range(n2):
    elem = input("Enter element : ")
    list2.append(elem)
result = []
for i in list1:
    result.append(i)
for i in list2:
    result.append(i)
result.sort()
print(result)