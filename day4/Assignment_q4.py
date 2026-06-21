tup = (5,2,6,7,8,9,1,21,55)
tup1=()
tup2=()
tup = list(tup)
tup1 = list(tup1)
tup2 = list(tup2)
for i in tup:
    if i%2==0:
        tup1.append(i)
    else:
        tup2.append(i)
tup1= tuple(tup1)
tup2= tuple(tup2)
print(tup1)
print(tup2)