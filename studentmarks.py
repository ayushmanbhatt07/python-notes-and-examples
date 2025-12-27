'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''
s1=int(input("enter the marks in first subject: "))
s2=int(input("enter the marks second subject: "))
s3=int(input("enter the marks in third subject: "))
tot=(s1+s2+s3)/300
s11=s1/100
s22=s2/100
s33=s3/100
if((tot>=0.40)and(s11>=0.33)and(s22>=0.33)and(s33>=0.33)):
    print("passed")
else:
    print("fail")