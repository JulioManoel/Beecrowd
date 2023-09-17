num = int(input())

cobaias = [0, 0, 0]

for i in range(num):
  text = input().split()
  if text[1] == 'C': cobaias[0] += int(text[0])
  elif text [1] == 'R': cobaias[1] += int(text[0])
  else: cobaias[2] += int(text[0])

total = sum(cobaias)
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {cobaias[0]}')
print(f'Total de ratos: {cobaias[1]}')
print(f'Total de sapos: {cobaias[2]}')
print(f'Percentual de coelhos: {(cobaias[0]/total)*100:.2f} %')
print(f'Percentual de ratos: {(cobaias[1]/total)*100:.2f} %')
print(f'Percentual de sapos: {(cobaias[2]/total)*100:.2f} %') 