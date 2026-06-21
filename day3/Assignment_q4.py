# Q4. Write a function to return the count the  number of digits in a number, n.
n = int(input("Enter your number: "))
count =0
while(n!=0):
    count+=1
    n=int(n/10)
print(count)