# Q2. Write a function that takes two integers a and b and prints all even 
# numbers between them (inclusive).
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
for i in range(a,b+1,1):
    print(i)