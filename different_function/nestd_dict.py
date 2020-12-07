students={
    100:{"rol":100,"name":"test","course":"bca","total":140},
    101:{"rol": 101, "name": "test1", "course": "mca", "total": 140},
    102:{"rol": 102, "name": "test2", "course": "bca", "total": 140},
    103:{"rol": 103, "name": "test3", "course": "bca", "total": 140},

}
def print_student(**kwargs):
    rol=kwargs["id"]
    if(rol in students):
        print(students[rol]["name"])
        prop=kwargs["prop"]
        if(prop in students[rol]):
            print(students[rol][prop])
        else:
            print("invalid")

id=int(input("enter id"))
prop=input("enter property")
print_student(id=id,prop=prop)