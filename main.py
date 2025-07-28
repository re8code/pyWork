op = []
op.append(lambda a, b: a + b)
op.append(lambda a, b: a - b)
op.append(lambda a, b: a * b)
op.append(lambda a, b: a / b)
op.append(lambda a, b: a % b)

index = 0
n, m = 70, 30
for i in range(5):
    index += 1
    print(f'{index}) operation result: {op[i](n, m)}')

print('vs'); index = 1

for func in op:
    print(f'{index}) operation result: {func(n, m)}')
    index += 1
