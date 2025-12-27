number=[10,20,25,30,32,37]
def even(x):
    return x%2==0
even=list(filter(even,number))#return type of filter function is boolean
print(even)