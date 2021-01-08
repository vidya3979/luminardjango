first =[1,2,3]
second =[4,5,6]

pairs=[(i,j) for i in first for j in second]
print(pairs)


#squares

f=[1,2,3,4]

squares=[i**2 for i in f]
print(squares)


lst=[1,2,3,4,6,7]

#output 012378
#num<5 num-1 and num>5 num+1

data=[i-1 if i<5 else i+1for i in lst]

print(data)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#output=1,2,3,4,5,6,7,8,9

#flatten operation

flat=[j for i in matrix for j in i]
print(flat)
