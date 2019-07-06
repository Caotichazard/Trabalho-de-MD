Problema: Summation of primes

Metodologia: 
    A solução desse exercicio é direta e simples, achar todos os primos e então soma-los.Foi utilizado o Crivo de Eratóstenes para de forma mais eficiente encontrar todos os número primos até dois milhões e então somalos.





Resultados e discussões:
    def achaPrimos(limite):#Função que ira procurar todos os primos menores que um certo limite
        primos=[True for n in range(limite+1) ]#cria uma lista com n=limite elementos e os atribui o valor logico True
        crivo=2#cria uma chave do primeiro número primo
        saida = []#lista de saida
        while  crivo*crivo <= limite:#enquanto o quadrado da cahve for menor que o limite, o loop ocorre
            if(primos[crivo]==True):#verifica se a chave é um primo
                for i in range(crivo*2,limite+1,crivo):#procura todos os números multiplos da chave
                    primos[i]=False#os transforma em falso, ou seja, não primos
            
            crivo += 1#aumenta a chave
        
        for i in range(2,limite):#Traduz o indice dos elemento primos para uma lista de elementos
            if primos[i]==True:
                saida.append(i)

        return saida
                

    primos = achaPrimos(2000000)
    soma = 0
    for i in primos:#realiza a soma de todos os elementos
        soma += i


    print(soma)
    A saida do programa foi 142913828922 como no arquivo de respostas fornecido

Conclusões finais:  
    Para realizar esse programa, era necessário um algortimo para achar número primos mais eficiente que a checagem pela definição, portanto a escolha do crivo, além disso foi mais incentivado o uso de tal algoritmo por temos um valor limite.
    
