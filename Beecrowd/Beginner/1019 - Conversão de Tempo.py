s = int(input())

m = s // 60
h = m // 60
m %= 60
s %= 60
print(f'{h}:{m}:{s}')