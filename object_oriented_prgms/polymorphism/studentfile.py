class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_student(self):
        print("name=",self.name,"age=",self.age)
    def __str__(self):
        return self.name


st=student("john",44)
st1=student("tom",34)
st2=student("can",30)

print(st)
print(st1)
print(st2)
