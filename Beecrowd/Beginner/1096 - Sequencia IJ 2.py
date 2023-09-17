i = 1
j = 7
while True:
  print(f'I={i} J={j}')
  if i == 9 and j == 5: break
  
  j -= 1

  if j < 5:
    j = 7
    i += 2