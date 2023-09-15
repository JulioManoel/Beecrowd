# Consumo

Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

## Entrada

O arquivo de entrada contém dois valores: um valor inteiro **X** representando a distância total percorrida (em Km), e um valor real **Y** representando o total de combustível gasto, com um dígito após o ponto decimal.

## Saída

Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| 500 <br/> 35.0           | 14.286 km/l              |
| 35.0                     |                          |

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| 2254                     | 18.119 km/l              |
| 124.4                    |                          |

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| 4554                     | 9.802 km/l               |
| 464.6                    |                          |

## Resolução

```python
km = float(input())
l = float(input())
print(f'{km/l:.3f} km/l')
```