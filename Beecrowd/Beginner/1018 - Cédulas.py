total = int(input())

num = total
nota100 = num // 100
num %= 100

nota50 = num // 50
num %= 50

nota20 = num // 20
num %= 20

nota10 = num // 10
num %= 10

nota5 = num // 5
num %= 5

nota2 = num // 2
num %= 2

nota1 = num // 1
num %= 1

print(total)
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
