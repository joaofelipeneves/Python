#funçã zip, compacta as 2 lista e coloca em uma lista só

lista1 = [1,2,3, 4,5]
lista2 = ["joao", "neves", "ribeiro", "gui", "paulo"]
lista3 = ["2,00", "5,00", "10,00", "20", "90"]

for numero, nome, valor in zip(lista1,lista2, lista3):
    print(numero,nome, valor)

