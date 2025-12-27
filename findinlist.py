# Write a program which finds out whether a given name is present in a list or not.
list=[]
name=input("enter a name: ")
list.append(name)
name=input("enter a name: ")
list.append(name)
name=input("enter a name: ")
list.append(name)
name=input("enter a name: ")
list.append(name)
find=input("enter the name to be searched: ")
if(find in list):
    print("found")
else:
    print("not found")