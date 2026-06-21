import random
secret_number = random.randint(1, 100)
while True:
    guess =int(input("Guess the secret number (between 1 and 100): "))
    if guess> secret_number:
        print("Too high")
    elif guess<secret_number:
        print("Too low")
    else:
        print("Correct! You guessed it!")
        break


 



