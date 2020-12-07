f=open("movies.csv","r")

dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")

    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict)

high=max(dict,key=dict.get)
print(high,dict.get(high))
