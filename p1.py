


primo_atual = 3
primos = [2]
eh_primo = 1
while( len(primos) != 10001):
	eh_primo = 1
	primo_atual = primo_atual + 2
	for n in primos:
		if primo_atual%n == 0:
			eh_primo = 0	
	if eh_primo == 1:
		primos.append(primo_atual)
		
print(primos[10000])

