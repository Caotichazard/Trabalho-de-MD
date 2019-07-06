#include<stdlib.h>
#include<stdio.h>

int achaNumeroTriangular(int pos, int num_anterior);
int achaQtdDivisores(int num);


int main(){
    int divisores=0;
    int pos_atual = 0;
    int num_atual=0;
    while (divisores <500)
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
        if(num%i==0){
            cont++;
        }
    }
    return cont;
}