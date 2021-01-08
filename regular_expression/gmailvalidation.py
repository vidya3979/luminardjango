
f=open("gmail_id")
fout=open("validgmailid","w")

mailid=set()
for gmailid in f:
    mailid.add(gmailid.rstrip("\n"))

from re import *

rule='[a-zA-Z0-9][a-zA-Z0-9._]{5,29}'+"@gmail.com"

for mail_id in mailid:

    matcher=fullmatch(rule,mail_id)
    if matcher!=None:
        fout.write(mail_id+"\n")
    else:
        pass