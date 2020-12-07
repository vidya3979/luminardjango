
pattern="A B A B A B C"

#find first recursive character (A)
#word count

dict={}
words=pattern.split(" ")
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

print(dict)


for word in words:
    if word[0]=="A":
        dict[word]+=1
    else:
        break
 print(dict)


