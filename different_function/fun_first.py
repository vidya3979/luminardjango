'''def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print(sum)

add(10,20)
'''
def print_data(**num):
    for k,v in num.items():
        print(k,v)
print_data(birth_place="kochi",desi="develop",salary=5000)
