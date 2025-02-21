def multi(*nums):
    total = 1
    for i in nums:
        total *= i
    return total

def éPar(*nums):
    for i in nums:
        if i % 2 == 0:
            print(f'{i} é par!')
        else:
            print(f'{i} é impar!')

print(éPar(1,2,3,4,5,6,7))

