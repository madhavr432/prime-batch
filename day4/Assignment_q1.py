str = input("Ener the string: ")
rev = ""
for char in str:
    rev = char + rev 
if rev == str:
    print("the string is palindrome")
else:
    print("the string is not palindrome")