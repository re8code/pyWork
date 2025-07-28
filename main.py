n, m = 70, 30

add = lambda a, b: a + b
print(f'1) {n} + {m} = {add(n, m):4d}', type(add))

sub = lambda a, b: a - b
print(f'2) {n} - {m} = {sub(n, m):4d}', type(sub))

print(f'3) {n} x {m} = {(lambda a, b: a * b)(n, m):4d}')
print(f'4) {n} / {m} = {(lambda a, b: a / b)(n, m):.2f}')

def rem(a, b):
    return a % b

print(f'5) {n} % {m} = {rem(n, m):4d}', type(rem))
