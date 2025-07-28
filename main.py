def delegator(n, m, op):
    if   op == 0: return (lambda a, b: a + b)(n, m)
    elif op == 1: return (lambda a, b: a - b)(n, m)
    elif op == 2: return (lambda a, b: a * b)(n, m)
    elif op == 3: return (lambda a, b: a / b)(n, m)
    else:         return (lambda a, b: a % b)(n, m)

a, b = 70, 30

print(f'1) {a} + {b} = {delegator(a, b, 0):4d}')
print(f'2) {a} - {b} = {delegator(a, b, 1):4d}')
print(f'3) {a} x {b} = {delegator(a, b, 2):4d}')
print(f'4) {a} / {b} = {delegator(a, b, 3):.2f}')
print(f'5) {a} % {b} = {delegator(a, b, 4):4d}')
