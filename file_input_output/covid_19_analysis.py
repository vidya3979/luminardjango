f=open("covid_19_india.csv","r")

dict={}

for lines in f:

    words=lines.rstrip("\n").split(",")
#    print(words)
 #   break

    state=words[3]
    confirmed_cases=int(words[8])
   # print(state,confirmed_cases)
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases

lst=[]

for k,v in dict.items():

    lst.append((v,k))
print(sorted(lst,reverse=True))
   # print(k,"===>",v)

high=max(dict,key=dict.get)
print(high,dict[high])




