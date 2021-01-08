class student:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total

    def print_student(self):
        print("roll no.=",self.rol)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)

obj=student(100,"tom","mca",140)
obj1=student(101,"ram","bca",200)
obj.print_student()
obj1.print_student()
