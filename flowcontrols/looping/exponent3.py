num=int(input("enter the num"))
total=0
while(num!=0):
    digit=num%10
    total=total+(digit**3)
    num//=10
print(total)