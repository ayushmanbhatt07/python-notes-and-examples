import re
text="python and java AND c++ are lang"
pattern=r"\w+"
#matches all characters only. no special symbols included and returns a list
matches=re.findall(pattern,text)
print(matches)

text="python and java AND c++ are lang"
pattern1=r"[\w+]+"
matches1=re.findall(pattern1,text)
print(matches1)