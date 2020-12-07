students=[
    [100,"arun","bca",145],
    [101,"varun","bca",140],
    [102,"arjun","mca",155],
    [103,"jeena","bcom",125],
    [104,"jiju","mca",145],

]

#print students names

for student in students:
    print(student[1])


#print total of all students

total=0
for student in students:
    total=total+student[3]
print(total)


#list the details of students those who are mca

for student in students:
    if student[2]=="mca":
        print(student)


#mca? bca? bcom? how many students seperately

mtotal=btotal=bctotal=0
for student in students:
    if student[2]=="mca":
        mtotal+=1
    elif student[2]=="bca":
        btotal+=1
    elif student[2]=="bcom":
        bctotal+=1
print("number of students in mca",mtotal)
print("number of students in bca",btotal)
print("number of students in bcom",bctotal)
