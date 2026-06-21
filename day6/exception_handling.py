try:
    x = int(input("enter x: "))
    ans = 10/x
except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")
except ValueError:
    print("please enter integer value")
else:
    print(f"ans = {ans}")
finally:
    print("End of program")