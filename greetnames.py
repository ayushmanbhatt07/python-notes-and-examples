'''Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.'''
l = ["Rohan", "Soham", "Sachin", "Rahul"]
for i in range(0,4):
    str=l[i]
    a=str.startswith('S')
    if(a==True):
        print("good afternoon",str)
    
    