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
s1 = set(list1)
s2 = set(list2)
if s1.intersection(s2) ==set():
    print("no common elements")
else:
    print(s1.intersection(s2))