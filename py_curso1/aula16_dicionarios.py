#dicionarios
dic = {"a":"abelha", "b":"bola" , "c":"casa"}
print(dic["a"])

for chave in dic:
    print(chave)
    print(dic[chave])
    print(chave+ ":"+ dic[chave])

for i in dic.items():
    print(i)

for j in dic.keys():
    print(j)