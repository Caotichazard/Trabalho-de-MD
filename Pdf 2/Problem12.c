Problema: Highly divisible triangular number

Metodologia:
	Um número triangular na posição N é a soma de todos os naturais menores que N, pensando nisso, foi necessário criar uma forma para encontrar o número triangular de posição N, e então criar uma forma de testar seus divisores.

Resultados e discussões:

	#include<stdlib.h>
	#include<stdio.h>

	int achaNumeroTriangular(int pos, int num_anterior);//Função que encontra o número de posição N utilizando o numero da posição N-1
	int achaQtdDivisores(int num);//Função que acha o numero de divisores de um número


	int main(){
	    int divisores=0;//contador de divisores
	    int pos_atual = 0;//posição atual a ser considerada
	    int num_atual=0;//Numero triangular da posição atual
	    while (divisores <500)// Realiza a operação ate o contador de divisores atinga 500 ou mais
	    {   
		
		num_atual = achaNumeroTriangular(pos_atual,num_atual);
		divisores = achaQtdDivisores(num_atual);
		
		pos_atual++;
	    }
	    printf("\n resultado: %d\n",num_atual);
	    
	    
	}

	int achaNumeroTriangular(int pos, int num_anterior){
	    return pos+num_anterior;
	}

	int achaQtdDivisores(int num){
	    int cont=0;
	    for(int i=1;i<=num;i++){
		if(num%i==0){//verifica se o resto da divisão é zero o que o caracteriza como divisor
		    cont++;
		}
	    }
	    return cont;
	}

	O retorno desse algoritmo foi de 76576500 correspondendo com a resposta fornecida

Considerações finais:
	A soluçao desse problema era bem direta e facil de se implementar, o que tornou viavel usar a linguagem C para isso pois ela poderia realizar em um menor tempo as operações em comparação a python. Além disso outra otimização foi o uso do numero anterior para calcular o numero da posição atual pois assim se tornava um operção simples o que acelerava o processo.
