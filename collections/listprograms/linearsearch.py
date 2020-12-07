lst=(1,2,3,4,5,6,7,8)

element=int(input("enter the element"))
flg=0
for num in lst:
    if element==num :
        flg+=1
        break
    else:
        flg=0

    if(flg==0):
        print("element not found")
    else:
        print("element found")

  # if(element in lst):
  #      print("element found")
   # else:
    #    print("element not found")
