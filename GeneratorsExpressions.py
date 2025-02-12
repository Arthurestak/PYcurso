from sys import getsizeof


# Lista comum -> Quanto maior, maior o peso
numeros = [x * 10 for x in range(1000000)]
print(numeros)
print(getsizeof(numeros))


# Generator Expression -> Muito mais leve, peso único
numeros = (x * 10 for x in range(1000000))
print(numeros)
print(getsizeof(numeros))