# Q8.  Letʼs create a Simple Calculator that performs arithmetic operations. Create 
# a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.
def calculator(a,b,operation):
    if (operation=='+'):
        print(a+b)
    elif (operation=='/'):
        print(a/b)
    elif (operation=='*'):
        print(a*b)
    elif(operation=='-'):
        print(a-b)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
op = input("Enter the operation you want to perform: ")
calculator(a,b,op)