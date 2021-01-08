







from re import *

rule='KL\d{2}[A-Z]{2}\d{1,4}'

vehiclenum=input("enter the veh no.")

matcher=fullmatch(rule,vehiclenum)
if matcher!=None:
    print("valid veh num")
else:
    print("invalid")

