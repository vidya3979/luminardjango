class person:
    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_person(self):
        print("name=",self.name)
        print("age=",self.age)
        print("gender=",self.gender)


obj=person()
obj.set_person("ajay",25,"male")

obj1=person()
obj1.set_person("ravi",30,"male")

obj.print_person()
obj1.print_person()

