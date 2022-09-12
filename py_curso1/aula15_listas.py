lista = ["aba", "mel", "toma"]
print(lista)
lista2 = [1,2,3,4,5]
print(lista2)
#pode ser misturado

print(lista[2])

for item in lista:
    print(item)

tam = len(lista)
print(tam)

#adiciona um elemento novo no index
lista.append("limão")
print(lista)

if  3 in lista2:
    print("7 ta")

#remover elementos da lista
del lista[2:]
print(lista)

del lista[:]
print(lista)

lista4= []
lista4.append(23)
print(lista4)


#lista parte 2 - ordenação
lista1 = [123, 124, 125 , 2 , 5, 7]
lista1.sort()
print(lista1)

sorted(lista1)
print(lista1)

lista1.sort(reverse=True)
print(lista1)

lista1.reverse()
print(lista1)

#com strings isso tambem funciona
#sorte vai alfabeticamente

