nota = list(map(float, input().split()))
media = ((nota[0]*2) + (nota[1]*3) + (nota[2]*4) + (nota[3]*1)) / 10
print(f'Media: {media:.1f}')

if media >= 7.0:
  print('Aluno aprovado.')

elif media >= 5:
  print('Aluno em exame.')
  notaExame = float(input())
  print(f'Nota do exame: {notaExame:.1f}')
  media = (media + notaExame) / 2

  if media >= 5:
    print('Aluno aprovado.')
    print(f'Media final: {media:.1f}')
  
  else:
    print('Aluno reprovado.')

else:
  print('Aluno reprovado.')