
from functools import*

class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name

f= open("emp_details1","r")

employees=[]
for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")
    employees.append(employee(id,name,exp,salary,desig))

#find hihest salary

highestsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                 list(map(lambda emp:emp.salary,employees)))

print(highestsal)

#hihest sal deatail of emp

employee=list(filter(lambda emp:emp.salary==highestsal,employees))

for emp in employee:
    print(emp.name)

#highest sal whose desig is developer

high_develop=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                    list(map(lambda emp:emp.salary,
                    list(filter(lambda emp:emp.desig=="developer",employees))
                    ))
                    )
print(high_develop)


