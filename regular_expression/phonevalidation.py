f=open("phonenumbers")
fout=open("validphonenum","w")

phnum=set()
for numbers in f:
    phnum.add(numbers.rstrip("\n"))

from re import *

rule='\d{10}'
for phonnumbers in phnum:
    matcher=fullmatch(rule,phonnumbers)
    if matcher!=None:
        fout.write(phonnumbers+"\n")
    else:
        pass
