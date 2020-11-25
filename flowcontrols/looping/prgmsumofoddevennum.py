lowlimit=int(input("enter lower limit"))# 1
uplimit=int(input("enter upper limit"))#10
sum_even=0
sum_odd=0
while(lowlimit<=uplimit):
    if(lowlimit%2==0):
        sum_even=sum_even+lowlimit
    else:
        sum_odd=sum_odd+lowlimit
    lowlimit+=1
print("sum of even numbers",sum_even)
print("sum of odd numbers",sum_odd)
