#exercicios
#exericio 1 : pegar uma idade e ver se a pessoa eh maior de idade
print("escreva a sua idade:")
idade = int(input())

if idade >= 18:
    print("eh maior de idade")

if (idade < 18):
        print("eh menor de idade")

#exercicio 2 : receba 2 notas , faça a aritmetica e se > 6 escreva aprovado

print("escreva a nota 1:")
nota1 = int(input())
print("escreva a nota 2 :")
nota2 = int(input())

final = ((nota1 + nota2)/2)

if (final > 6):
    print("aprovado")
elif (final < 6):
    print("reprovado")

#exercicio 3 : pegue uma lista e ordene
lista= [23 , 9, 100]
lista.sort()
print(lista)

#exercicio 4 :
nmr1 = int(input("coloque o primeiro numero"))
nmr2 = int(input("coloque o segundo numero"))

sinal = input("coloque o sinal ")

if (sinal == "+"):
    print(nmr1 + nmr2)
if (sinal == "-"):
    print(nmr1 - nmr2)
if (sinal == "*"):
    print(nmr1 * nmr2)
if (sinal == "/"):
    print(nmr1 / nmr2)