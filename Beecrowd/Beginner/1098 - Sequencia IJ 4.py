i = 0
j = 1
for aux in range(11):

  for test in range(3):
    if 0.8 < i < 1.2 or i == 0 or i > 1.8: print(f'I={i:.0f} ', end='')
    else: print(f'I={i:.1f} ', end='')

    if 0.9 < j < 1.1 or 1.9 < j < 2.1 or 2.9 < j < 3.1 or 3.9 < j < 4.1 or 4.9 < j < 5.1: print(f'J={j:.0f}')
    else: print(f'J={j:.1f}')
    j += 1
  
  i += 0.2
  j -= 2.8
    