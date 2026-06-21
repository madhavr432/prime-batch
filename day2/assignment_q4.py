# Q4. The user enters a string containing a number (e.g.,"45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.
a = input("Enter your string: ")
a= int(a)
print(a, type(a))
a= float(a)
print(a, type(a))
a= str(a)
print(a, type(a))