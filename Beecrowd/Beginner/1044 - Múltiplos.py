num = list(map(int, input().split()))

if num[1] % num[0] == 0 or num[0] % num[1] == 0: print('Sao Multiplos')
else: print('Nao sao Multiplos')