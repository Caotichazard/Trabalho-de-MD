Problema: Power digit sum

Metodologia:
	O objetivo era encontrar a soma de todos os digitos de 2^1000, portanto, uma maneira simples era dividir o numero por potencias de 10, somar o resto da divisão a soma dos digitos, e então subtrair esse resto do numero inicial, e então aumentar a potencia de 10. 


Resultados e discussões:

	x = 2**1000#numero a ser usado
	div = 10#potencia de 10 inicial
	aux = 0
	aux2 = 1
	soma = 0#soma final dos digitos
	while(x>0):#realiza o loop até que o numero inicial seja 0

	    aux = x%div#armazena o digito a ser recebido nessa iteração
	    soma = soma+ (aux/aux2)#soma o digito a soma total, é usado um auxiliar para garantir que o numero seja unitário 
	    x = x - aux#remove o resto do número
	    aux2 =div# atualiza as potencias para poder continuar a operação
	    div = div*10

	print(soma)
	O resultado desse algoritmo foi 1366 igual ao resultado fornecido no arquivo de respostas

Considerações finais:
	A solução desse problema é simples porém é necessário uma estrutura muito flexível para comportar o número 2^1000,ja que esse requer cerca de 1000 bits para armazenar, então, ao contrario da minha decisão inicial, foi necessário o uso de python para essa operação.
