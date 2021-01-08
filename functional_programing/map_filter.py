lst=[10,11,12,13,14,15]

squares=list(map(lambda num:num**2,lst))
print(squares)

cubes=list(map(lambda num:num**3,lst))
print(cubes)

even=list(filter(lambda no:no%2==0,lst))
print(even)
