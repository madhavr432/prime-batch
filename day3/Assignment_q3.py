# Q3. Write a function that prints the digits of a number, 
n = int(input("Enter your number: "))
while(n!=0):
    print(n%10)
    n=int(n/10)