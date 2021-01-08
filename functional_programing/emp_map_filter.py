employees=["ajay","vijay","anil","danie","tom","joy"]

upper=list(map(lambda emp:emp.upper(),employees))
print(upper)

ename=list(filter(lambda name:name[0]=="a",employees))
print(ename)