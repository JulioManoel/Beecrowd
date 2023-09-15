num = list(map(float, input().split()))

print(f'TRIANGULO: {(num[0]*num[2])/2:.3f}')
print(f'CIRCULO: {3.14159*num[2]**2:.3f}')
print(f'TRAPEZIO: {((num[0]+num[1])*num[2])/2:.3f}')
print(f'QUADRADO: {num[1]**2:.3f}')
print(f'RETANGULO: {num[0]*num[1]:.3f}')