class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name

f=open("employee","r")
lst=[]

for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")
    obj=employee(id,name,exp,salary,desig)
    lst.append(obj)

for emp in lst:
    print(emp)
