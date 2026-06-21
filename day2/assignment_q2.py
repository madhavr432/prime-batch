# Q2. Take two numbers as input from the user and print their sum, difference, product, and quotient.
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print("The sum of given two numbers is: ", a+b)
print("The product of given two numbers is: ", a*b)
if a>b :
    print("The difference of given two numbers is: ", a-b)
    c=int(a/b)
    print("The quotient of given two numbers is: ", c*b)
else :
    print("The difference of given two numbers is: ", b-a)
    c=int(b/a)
    print("The quotient of given two numbers is: ", c*a)