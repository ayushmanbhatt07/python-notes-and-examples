'''
number=[10,20,25,30,32,37]
def even(x):
    return x%2==0
even=list(filter(even,number))
print(even)
'''
number=[10,20,25,30,32,37,-1]
even=list(filter(lambda x: x%2==0,number))#inbuilt function lambda
n=list(filter(lambda x: x<0,number))
# lambda is an anonymous function
print(n)
print(even)

sum=lambda x,y:x+y#sum is a function here
print(sum(10,20))


#program to pass lambda function as an argument
def func(f,n):
    print(f(n))
twice= lambda x: x*2
thrice=lambda x: x*3
func(twice,4)
func(thrice,6)