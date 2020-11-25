#given three input n, min&max find the number of vlues raised to the nth power range.
#eg: num=2
#min=1
#max=40






n=int(input("enter the num"))
min=int(input("enter the minimum"))
max=int(input("enter the maximum"))
for i in range(1,max+1):
    if i**n in range(min,(max+1)):
        print(i,"," ,i,"^",n,"=",i**n)