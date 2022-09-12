import random

#escolhe sempre um mesmo numerorandom.seed(1)
nmbr = random.randint(0, 10)
print(nmbr)

lista = [6, 45 , 9]
nmbr2 = random.choice(lista)
print(nmbr2)