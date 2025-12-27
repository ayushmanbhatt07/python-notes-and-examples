'''Write a python function to print first n lines of the following pattern:
***
**  for n 
*
'''
def pat(n):
    while(n>0):
        print("*"*n)
        n=n-1
n=int(input("enter the number of lines: "))
pat(n)