

from re import*

#pattern="a+"
#pattern="a*"
#pattern="a?"
pattern="^a"
#pattern="a$"
#pattern='a{2,3}'


#matcher=finditer(pattern,"aaaabaabaaaabaa")

matcher=fullmatch(pattern,"baaabaabaaaa")
if matcher!=None:
    print("given string starting with a")
else:
    print("given string not starting with a")