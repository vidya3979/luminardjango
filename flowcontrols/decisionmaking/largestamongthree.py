num1 = int(input("enter the value for num1"))
num2 = int(input("enter the value for num2"))
num3 = int(input("enter the value for num3"))
if((num1>num2)&(num1>num3)):
    print("num1 is largest number")
elif((num2>num1)&(num2>num3)):
    print("num2 is largest number")
elif((num3>num1)&(num3>num2)):
    print("num3 is largest number")
else:
    print("3 numbers are equal")