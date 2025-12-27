import re
pattern=r"\d+"
matches=list(re.finditer(pattern,"LXI 2013, VXI 2015,VDI 93480934"))
# for match in matches:
    # print(match.group())