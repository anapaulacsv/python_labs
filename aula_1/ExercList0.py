numeros = [1,4,9,16,25]
numeros_maior_1 = numeros
numeros_maior_1.append(42) 
print(numeros) 
print(numeros_maior_1)
numeros_maior_2 = numeros +[42]
print(numeros_maior_2)
print(numeros)
numeros_menor_1 = numeros [2:]
numeros_menor_2 = numeros 
del numeros_menor_2 [:2]
print(numeros_menor_2) #Não ta operando em uma nova lista
print(numeros) #Foi deletado os 2 primeiros tbm

numeros.extend([1,2,3])
print(numeros)
numeros.extend("kgfff")
print(numeros)
numeros_maior_1.append([3,3,3]) 
print(numeros)
numeros.insert(1,'here')
print(numeros)
numeros.insert(20,'end')
print(numeros)
numeros.insert(-1,'e')
print(numeros)

numeros = 2* numeros 
print(numeros)