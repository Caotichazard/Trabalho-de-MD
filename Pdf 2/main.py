
def achaPrimos():
    primo_atual = 3
    primos = [2]
    eh_primo = 1
    total = 0
    while( primo_atual < 2000000):
       
        eh_primo = 1
        primo_atual = primo_atual + 2
        for n in primos:
            if primo_atual%n == 0:
                eh_primo = 0	
        if eh_primo == 1:
            primos.append(primo_atual)


    return primos
            
import time
start = time.time()

primos = achaPrimos()
soma = 0
for i in primos:
    soma = soma + i


print(soma)

end = time.time()
print(end-start)