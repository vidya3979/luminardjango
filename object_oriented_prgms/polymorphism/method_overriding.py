class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print("name=",self.name,"\t","age=",self.age)
    def __str__(self):
        return self.name

p=person("ajay",22)
p1=person("ravi",24)
print(p)
