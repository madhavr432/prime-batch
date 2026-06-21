# Q7. Design a program to continuously input a number n from user & print if it is 
# positive or negative until the user enters “Quit”.
while True:
    user_input = input("Enter the value of n: ")
    if(user_input=='Quit'):
        break
    n = int(user_input)
    if (n>0):
        print("The number is positive ")
    elif (n==0):
        print("The number is zero ")  
    else:
        print("The number is negative ")
    