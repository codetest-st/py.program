'''enter a number and count its digit'''
num=int(input("enter a num:"))
x=0
while num>0:
    x=x+1
    num=num//10
print(f"total digit in the number is{x}")