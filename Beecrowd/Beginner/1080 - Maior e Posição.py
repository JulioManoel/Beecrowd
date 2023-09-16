num = []

for i in range(100):
  num.append(int(input()))

value, index = max((value, index) for index, value in enumerate(num))
print(value)
print(index+1)