def soma(*nums):
    total = 0 
    for i in nums:
        total += i
    return total

num1 = soma(1,2)
print(num1)

numeros = 1,2,3,4,5,6,7,8,9,10

print(soma(*numeros))