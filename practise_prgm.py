lst=[1,2,3,4,5,6,7,8]
element=int(input("enter the element"))
flg=0
for num in lst:
    if(element==num):
        flg+=1
        break
    else:
        flg=0
        if (flg==0):
            print("element found in list")
        else:
            print("not found in list")
