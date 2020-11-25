number=int(input("enter number"))
flg=0
for i in range(2,number):
    if(number%i==0):
        flg+=1
        break
if(flg==0):
    print("prime")
else:
    print("not prime")
