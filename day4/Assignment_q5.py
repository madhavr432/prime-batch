dict = {
    "kundan": 99,
    "madhav" : 89,
    "manan" : 88,
    "keshav": 69,
    "karan": 83
}
while True:
    user_input= input("Enter the key: ")
    if user_input=='a':
        name = input("Enter the name of student: ")
        marks = int(input("Enter the marks of student: "))
        dict.update({name : marks})
    elif user_input=='b':
        name = input("Enter the name you want to change: ")
        dict[name]= int(input("Enter the new marks of student: "))
    elif user_input=='c':
        name = input("Enter the name of student you want to check for: ")
        print(dict[name])
    elif user_input=='d':
        print(dict)
    elif user_input == 'quit':
        break
