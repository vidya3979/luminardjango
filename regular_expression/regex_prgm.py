#regular expression

#pattern matching

import re

matcher=re.finditer("ab","ababababaabbab")

cnt=0
for match in matcher:
    print(match.start())
    #print(match.group())
    cnt+=1
print(cnt)
