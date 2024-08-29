from revisao.ex3 import calculadora


def somar(x,y):
    return x+y

print(somar(10,10))

####

c = calculadora(10,10)
print(c.somar())

####

soma = lambda x,y : x+y

soma(x,y)