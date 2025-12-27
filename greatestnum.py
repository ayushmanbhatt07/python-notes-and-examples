# Write a program to find the greatest of four numbers entered by the user.
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
d=int(input("enter the number: "))
if((a>b)and(a>c)and(a>d)):
    print("first number is greatest")
elif((b>a)and(b>c)and(b>d)):
    print("second number is greatest")
elif((c>a)and(c>b)and(c>d)):
    print("third number is greatest")
elif((d>a)and(d>b)and(d>c)):
    print("fourth n umber is the greatest")
else:
    print("all are equal")