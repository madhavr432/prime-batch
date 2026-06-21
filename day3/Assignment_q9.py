# Q9.Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5)+1,1):
        if(n%i == 0):
            return False
    return True
n = int(input("Enter the value of n: "))
if(is_prime(n)):
    print("The number is prime")
else:
    print("The number is not prime")


