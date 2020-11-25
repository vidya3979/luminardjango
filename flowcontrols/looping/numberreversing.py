'''num=int(input("enter num"))
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
'''

num=int(input("enter the num"))

res=0
while(num!=0):
    digit=num%10
    res=res*10+digit
    num=num//10
print(res)