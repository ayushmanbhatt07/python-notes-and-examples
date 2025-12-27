import re
pattern="[a-zA-Z]+ \d+"
'''
explanation:

'''
matches=re.findall(pattern,"LXI 2013,VXI 2015,VDI 20W63 , MARUTI SUZUKI")
print(matches)

pattern1=r"\w+ [-]?"
matches2=re.findall(pattern,"LXI 2013,VXI-2015,VDI 20W63 , MARUTI SUZUKI")
print(matches2)
