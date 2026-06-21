def search(nums, x):
    i = 0
    for val in nums:
        if(val ==x):
            return i
            break
        i+=1
    return False
nums = [1,2,3,10,4]
x = int(input("Enter the number you want to search for: "))
if(search(nums, x)==False):
    print("The number is not in list")
else:
    print("The index of number is ", search(nums, x))
