x = 2**1000
div = 10
aux = 0
aux2 = 1
soma = 0
while(x>0):

    aux = x%div
    print(aux/aux2)
    soma = soma+ (aux/aux2)
    x = x - aux
    aux2 =div
    div = div*10

print(soma)