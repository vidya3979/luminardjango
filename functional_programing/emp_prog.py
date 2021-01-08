class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.id +","+ self.name +","+ self.exp +","+ self.salary +","+ self.desig

f=open("emp_details1","r")
lst=[]


for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")
    obj=employee(id,name,exp,salary,desig)
    lst.append(obj)



for emp in lst:
    print(emp)

ename=list(map(lambda emp:emp.name.upper(),lst))
print(ename)

ename_desig=list(filter(lambda emp:emp.desig=="developer",lst))
for emp in ename_desig:
    print(emp)

sal= list(filter(lambda emp:int(emp.salary)>30000,lst))

for emp in sal:
    print(emp)