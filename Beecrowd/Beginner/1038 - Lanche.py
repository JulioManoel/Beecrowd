num = list(map(int, input().split()))
produts = [4, 4.5, 5, 2, 1.5]
print(f'Total: R$ {produts[num[0]-1] * num[1]:.2f}')