text="hai how are you hai how are you"


#word count => hai 2, how 2, are 2, you 2

dict={}

words=text.split(" ")
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
