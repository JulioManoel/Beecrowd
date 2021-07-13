#include <stdio.h>
 
int main() {
    char nome[20];
    double salario,comissao;
    scanf("%s",nome);
    scanf("%lf",&salario);
    scanf("%lf",&comissao);
    salario+=(comissao*0.15);
    printf("TOTAL = R$ %.2lf\n",salario);
    return 0;
}