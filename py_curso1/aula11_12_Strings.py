#-*- coding: utf-8 -*-
a = "diego"
b = "mariano"

nome = "diego marinho"
#juntar 2 palavras
concatenar = a + " " + b + "\n"
print(concatenar)

#ver quantos elementos existem na palavra
tamanho = len(concatenar)
print (tamanho)

#navegando pelo indice
print(a[2])
print(a[1])
print(a[4])

#imprimir uma parte de uma string, da letra 0 ate a 5
print(concatenar[0:5])

#aula 2 , alterando a caixa da palavra
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())

#função strip : tira caracteres especiais do inicio e do fim da frase
print(concatenar.strip())
#função split: quebra a string e retorna os idividuais, podendo ser especifica para o que está dentro do ()
print(concatenar.split("a"))

#busca na string
busca = nome.find("diego")
print(busca)
print(nome[busca:])

#mudar uma string
nome = nome.replace("diego", "diogo")
print(nome)