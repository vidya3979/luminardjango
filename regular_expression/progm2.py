from re import *
#predefined character sets/charaters

#pattern='[a-z]' #check characters

#pattern='[0-9]'# check numbers in pattern

#pattern = '[^0-9]' #check except all numbers

#pattern='[^a-z]' #check except all lowercase characters

#pattern='[a-zA-Z0-9]' #check all upercase lowercase and numbers

pattern='[^a-zA-Z0-9]' #check only special charaters
matcher=finditer(pattern,"abc Z@7k")
for match in matcher:
    print(match.start())
    print(match.group())
