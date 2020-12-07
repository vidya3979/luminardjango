lst=[21,20,18,22,7,2,25]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
flg=0
element=int(input("enter the element you want to search"))
while(low<upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if flg==0:
    print("no lement found")
else:
    print("element found")
