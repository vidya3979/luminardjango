

lst=[1,2,3,4]
no1=int(input("enter value1= "))
no2=int(input("enter value2= "))
#res=no1/no2        #if value 10/0 thn exception error comes
#print(res)
#print("i have one database transaction")
#print("i have one file transaction")

#so for this we use try: and except: and finally:


try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)

try:
    print(lst[3])
except Exception as e:
    print(e.args)
print("i have one database transaction")
print("i have one file transaction")