'''enter a number and print rev of digits'''
num=int(input("enter a num:"))
x=0
while num>0:
    x=x*10+num%10
    num=num//10
print(f"total digit in the number is{x}")