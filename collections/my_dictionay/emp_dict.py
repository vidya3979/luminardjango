employee={"eid":1000,"desig":"developer","exp":1,"company_name":"luminar"}

#print company name

print(employee["company_name"])

#checking salary key

print("salary" in employee)

#add a new key value pair salary 30000

employee["salary"]=30000
print(employee)

#add 5000 more in to current salary

employee["salary"]+=5000
print(employee["salary"])

#print all keys in the data

for keys in employee:
    print(keys)

#for print keys and values

for keys in employee:
    print(keys,",",employee[keys])





