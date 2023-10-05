#include <iostream>
#include <ctime>
#include <cmath>

// Função para calcular o número de Fibonacci usando unsigned long long
unsigned long long fibo(unsigned long long n) {
  return round(pow(1+sqrt(5)/2,n) / sqrt(5));
}

int main() {
  unsigned long long n = 5ULL;

  clock_t inicio = clock();

  unsigned long long resultado = fibo(n);

  clock_t fim = clock();
  std::cout << "Fibonacci(" << n << ") = " << resultado << std::endl;
  std::cout << "Tempo: " << static_cast<double>(fim - inicio) / CLOCKS_PER_SEC << " segundos" << std::endl;

  return 0;
}
