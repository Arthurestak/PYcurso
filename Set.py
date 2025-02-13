lista = [1,2,3,4]
lista1 = [1,2,3,4]
                                                #Int
lista_set = set(lista)
lista1_set = set(lista1)

print(lista_set & lista1_set) # Mostra apenas os que estão em comum 
print(lista_set | lista1_set) # Mostra os que estão em comum sem repetir - UNION
print(lista_set - lista1_set) # Mostra a diferença entre o primeiro e o segundo - DIFFERENCE
print(lista_set ^ lista1_set) # Mostra apenas os itens que não estão duplicados - SYMMETRIC DIFFERENCE

lista.update([1,2,3]) # Acrescenta os dados ao final da lista original
lista.add([1]) # Adiciona 1 ao final da lista
lista.remove(1) # Remove o número 1 da lista - Se não for digitado um valor existente na lista gerará um erro!
lista.discard(6) # Remove o item da lista - Se for digitado um valor não existente não gerará um erro!

#########################################################################
lista2 = ['a','b','c']
lista3 = ['a','b','c']
                                                #Str
lista2_set = set(lista2)
lista3_set = set(lista3)

print(lista_set.union(lista1_set)) # Mostra os que estão em comum sem repetir
print(lista_set.difference(lista1_set)) # Mostra a diferença do primeiro para com o segundo
print(lista_set.intersection(lista1_set)) # Mostra a interseção entre os envolvidos
print(lista_set.union(lista1_set)) # Mostra os que estão em comum sem repetir
print(lista_set.symmetric_difference(lista1_set)) # Mostra apenas os itens que não estão duplicados
