a={1,2,3,4,5}
b=a.copy()# allocates new memory to b that is creates a shallow copy
print(b)
b.add(6)#adds 6 to b only as b is a shaloow copy
print(b)
print(a)
