# Q9. Ask the user for:  Principal (P), Rate (R), Time (T). Convert all to  and 
# compute simple interest: 
# SI =(P ∗R∗T)/100
p = float(input("Enter the principal amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time period : "))
si = (p*r*t)/100
print("The simple intrest calculated is ", si)