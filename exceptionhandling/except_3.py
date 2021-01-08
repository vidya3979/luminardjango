no1=int(input("enter the value1= "))
no2=int(input("enter the value2= "))
try:
    res=no1/no2
    print(res)
except:
    no2 = int(input("enter the new value2= "))
    res=no1/no2
    print(res)
    try:
        res=no1/no2
        print(res)
    except:
        no2 = int(input("enter the new value2= "))
        res = no1 / no2
        print(res)
finally:
    print("i have one database transaction")
    print("i have one file transaction")
