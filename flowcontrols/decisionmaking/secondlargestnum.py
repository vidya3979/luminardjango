num1 = int(input("enter the value for num1"))
num2 = int(input("enter the value for num2"))
num3 = int(input("enter the value for num3"))

if((num1 > num2)&(num1 > num3)):
    if(num2>num3):
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)


elif((num2 > num1)&(num2 > num3)):
    if(num1>num3):
        print(num2, num1, num3)
    else:
        print(num2,num3,num1)

elif((num3 > num1)&(num3 > num2)):
    if(num1>num2):
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)

else:
    print("3 numbers are equal")