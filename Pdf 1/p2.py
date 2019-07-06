Problema: Special Pyhtagorian triplet

Metodologia:
	Uma tripla pitagorica é quando a soma dos quadrados de dois numeros é igual ao quadrado de um terceiro número, ou seja a²+b²=c².Para resolver esse problema foi usada a logica de que, C tem que ser o complemento da soma de A e B, e então de forma interativa foi testada as possibilidades dessa combinação


Resultados e discussões:
	soma = 1000#esse é o resultado da soma dos 3 numeros
	solucao = 0
	for a in range(1,soma+1):#Sera testada cada iteração a partir do caso base de A ser 1 ate A ser 1000 
		for b in range(a+1,soma+1):#então sera testado o B>A que então consiga satisfazer a solução
			c = soma - a - b
			if a*a + b*b == c*c:
				solucao = a*b*c

	print(solucao)
	A saida do programa foi 31875000, compativel com a resposta no arquivo fornecido.

Considerções finais:
	A solução desse problema foi difícil de se traduzir para codigo poís há varias soluções possiveis porém cada uma tem sua dificuldade de implementação, entretanto, a "ideia" da solução foi facil de se chegar.

