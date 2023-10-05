import time

def fibo(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)
        
n = 5
inicio = time.time()

print(fibo(n))

fim = time.time()
print(f"Tempo: {fim - inicio} segundos")