import math
import time

def fibo_binet(n):
  phi = (1 + math.sqrt(5)) / 2
  return round((phi ** n - (-phi) ** -n) / math.sqrt(5))

n = 5
inicio = time.time()

print(fibo_binet(n))

fim = time.time()
print(f"Tempo: {fim - inicio} segundos")

