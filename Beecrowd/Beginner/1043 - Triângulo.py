num = list(map(float, input().split()))

if num[0] < num[1]+num[2] and num[1] < num[0]+num[2] and num[2] < num[0]+num[1]:
  print(f'Perimetro = {num[0]+num[1]+num[2]:.1f}')
else:
  print(f'Area = {((num[0]+num[1])*num[2])/2:.1f}')
