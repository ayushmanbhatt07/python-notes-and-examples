"""Write a class “Calculator” capable of finding square, cube and square root of a 
number."""
class calculator:
    
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"{self.n*self.n}")
    def cube(self):
        print(f"{self.n**3}")
    def squareroot(self):
        print(f"{self.n**0.5}")
ch=float(input("enter 2.0 for square,3.0 for cube,0.5 for square root: "))
n=int(input("enter the number: "))
obj=calculator(n)
if(ch==2.0):
    obj.square()
elif(ch==3.0):
    obj.cube()
elif(ch==0.5):
    obj.squareroot()
else:
    print("wrong input")
