students={}

f=open("students","r")
for lines in f:
    rol,name,course,total=lines.strip("\n").split(",")

    if rol not in students:
        students[rol]={"rol":rol,"name":name,"course":course,"total":total}

print(students)

