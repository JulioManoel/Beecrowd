# O Maior

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

![](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png)

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

## Entrada

O arquivo de entrada contém três valores inteiros.

## Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 7 14 106            | 106 eh o maior    |

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 217 14 6            | 217 eh o maior    |

## Resolução

```python
num = list(map(int, input().split()))
print(f'{max(num)} eh o maior')
```