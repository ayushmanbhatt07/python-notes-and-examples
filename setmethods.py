
coder=set(['ankit','hjef','gyuefw','piyush'])
analysts=set(['dthdg','gtrgtr','frdvs','sgvfv','ankit','piyush'])
print("coders are:",coder)
print("analysts are: ",analysts)
print("person who can do both is",coder.intersection(analysts))
print("person working with us are ",coder.union(analysts))
print("people working as coder but not analysts are:",coder.difference(analysts))
