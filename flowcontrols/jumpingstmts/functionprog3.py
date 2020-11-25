def factorial(num1):
    fact=1
    for i in range(1,(num1+1)):
        fact=fact*i
    return fact

print (factorial(5))
