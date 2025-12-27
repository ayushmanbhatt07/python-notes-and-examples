''''Create an empty dictionary. Allow 4 friends to enter their favorite language as
 value and use key as their names. Assume that the names are unique.'''

dict={}
name=input("enter your name: ")
lang=input("enter your language: ")
dict.update({name:lang})
name=input("enter your name: ")
lang=input("enter your language: ")
dict.update({name:lang})
name=input("enter your name: ")
lang=input("enter your language: ")
dict.update({name:lang})

name=input("enter your name: ")
lang=input("enter your language: ")
dict.update({name:lang})
print(dict)