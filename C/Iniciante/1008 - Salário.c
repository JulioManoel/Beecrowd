#include <stdio.h>
 
int main() {
    int fun,horas;
    double valor;
    scanf("%i %i %lf",&fun,&horas,&valor);
    printf("NUMBER = %i\nSALARY = U$ %.2lf\n",fun,valor*horas);
    return 0;
}