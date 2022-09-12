#função reduce, pega todos os elementos de uma lista e executa uma ação com eles
from functools import reduce
def soma(x, y):
    return x+y

lista = [1,2, 3 , 4 ,5]

soma = reduce(soma, lista)
print(soma)