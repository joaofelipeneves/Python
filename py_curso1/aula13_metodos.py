def soma (x, y):
    return x+y

def multi(x, y):
    return x * y
s = soma (2, 2)
#se for dar um print x , nao vai funcionar pq o x is a local scope
print(s)
m = multi(3 , 4)
print(m)
print(soma(s, m ))
