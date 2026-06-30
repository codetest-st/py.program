'''enter a number and print sum of digits'''
num=int(input("enter a num:"))
x=0
while num>0:
    x=x+num%10
    num=num//10
print(f"total digit in the number is{x}")