# 1015 - Distância Entre Dois Pontos


Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =![](https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1015.png)

## Entrada

O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: _**x1 y1**_ e a segunda linha contém dois valores de ponto flutuante _**x2 y2**_.

## Saída

Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| 1.0 7.0 <br/> 5.0 9.0    | 4.4721                   |

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| -2.5 0.4 <br/> 12.1 7.3  | 16.1484                  |

| Exemplos de Entrada      | Exemplos de Saída        |
|--------------------------|--------------------------|
| 2.5 -0.4 <br/> -12.2 7.0 | 16.4575                  |

## Resolução

```python
p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))

x = (p2[0]-p1[0])**2
y = (p2[1]-p1[1])**2

print(f'{(x + y)**0.5:.4f}')
```