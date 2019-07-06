Problema: 10001st prime number

Metodologia: 
	Um primo é definido por ter apenas dois divisores, 1 e ele mesmo, nesse sentido, a solução seria uma aplicação direta da definição


Resultados e discussões:


	primo_atual = 3
	primos = [2]
	eh_primo = 1 #flag que verifica se o numero é primo ou não
	while( len(primos) != 10001):#loop ocorre enquanto não a lista de numeros primos é diferente a 10001
		eh_primo = 1
		primo_atual = primo_atual + 2#Considerando que o unico numero primo par é o numero 2, podemos então pular todos os numero pares e considerar apenas os impares
		for n in primos:#utilizando todos os primos anteriores
			if primo_atual%n == 0:#verificamos se o numero a ser analizado no momento não é divisivel por nenhum deles o que implicara que ele so tem um unico divisor alem de 1
				eh_primo = 0	
		if eh_primo == 1:#passando nos testes o numero é adicionado a lista
			primos.append(primo_atual)
			
	print(primos[10000])

	A resposta encontrada foi 104743 como conferido no arquivo de respostas fornecido

Considerações finais:
	Este tem uma solução bem direta porém pouco eficiente, certas escolhas como pular a verificação de numeros pares definitivamente reduzem o tempo de execução mas ainda sim não é possivel deixa-lo instataneo

