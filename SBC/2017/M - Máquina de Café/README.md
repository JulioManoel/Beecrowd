# Máquina de Café
O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expresso. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam muito tempo subindo e descendo escadas.

Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde trabalha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total gasto subindo e descendo escadas.

Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gasto pelos funcionários subindo e descendo escadas.

## Entrada
A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1 , A2 , A3 ≤ 1000), um por linha, onde Ai representa o número de pessoas que trabalham no i-ésimo andar.

## Saída
Seu programa deve imprimir uma única linha, contendo o número total de minutos a serem gastos com o melhor posicionamento possível da máquina.

| Exemplo de Entrada | Exemplo de Saída |
|--------------------|------------------|
| 10                 | 80               |
| 20                 |                  |
| 30                 |                  |

| Exemplo de Entrada | Exemplo de Saída |
|--------------------|------------------|
| 10                 | 60               |
| 30                 |                  |
| 20                 |                  |

| Exemplo de Entrada | Exemplo de Saída |
|--------------------|------------------|
| 30                 | 100              |
| 10                 |                  |
| 20                 |                  |

## Resolução

Uma abordagem direta e eficaz para resolver esse problema, dada a pequena quantidade de entradas (apenas três), é calcular todas as possíveis combinações. Essa abordagem é viável porque sabemos o número exato de entradas e ele é bastante baixo.

Para resolver o problema, primeiro identificamos todas as combinações possíveis de entrada, e então calculamos o tempo necessário para um funcionário se deslocar entre os andares A, B e C. É importante notar que, devido ao tempo de deslocamento, são necessários 2 minutos para que um funcionário se mova de um andar para outro, uma vez que ele deve retornar ao seu andar original após o deslocamento.

Em resumo, a solução envolve:
1. Listar todas as combinações possíveis das três entradas.
2. Para cada combinação, calcular o tempo total necessário para que os funcionários se desloquem entre os andares A, B e C, levando em consideração os 2 minutos extras para o retorno ao andar de origem.

Dessa forma, você poderá determinar o tempo mínimo necessário para que todos os funcionários se desloquem entre os andares com base nas três entradas disponíveis.

### Python
```python
a = int(input())
b = int(input())
c = int(input())

x = a*4 + b*2
y = b*2 + c*4
z = a*2 + c*2

min_time = min(x, y, z)
print(min_time) 
```

### C++
```c++
#include <bits/stdc++.h>

using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int x = a*4 + b*2;
  int y = b*2 + c*4;
  int z = a*2 + c*2;

  if(x < y && x < z) cout << x << endl;
  else if(y < z) cout << y << endl;
  else cout << z << endl;
}
```