dia = int(input())

ano = dia // 365
dia %= 365

mes = dia // 30
dia %= 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')