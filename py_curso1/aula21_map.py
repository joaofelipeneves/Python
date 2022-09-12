#função map
#função normal e errada
def dobro(x):
    return x*2
valor = [1,2 , 3 ,4 ,5]

print(dobro(valor))

#agora com a função map, map recebe 2 arugmentos uma eh a função e outro o obj
dobrado = map(dobro, valor)

for v in dobrado:
    print(v)
#era pra imprimir os valores mas nemfez isso

dobrado = list(dobrado)
print(dobrado)
