# Q10.Take a decimal number as input (like 45.78 ) and output its:
# • integer part - 45
# • fractional part -.78
n = float(input("Enter your number : "))
ip = int(n)
fp = n -ip 
print(n,ip,fp)