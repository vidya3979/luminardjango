

employee={}
f=open("emp_details","r")
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    employee[id]={"id":id,"name":name,"exp":exp,"salary":salary}
for k,v in employee.items():
    print(k,v)