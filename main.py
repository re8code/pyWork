def add (a, b): return a + b
def sub (a, b): return a - b
def mul (a, b): return a * b
def div (a, b): return a / b
def rem (a, b): return a % b

op = ['+', '-', 'x', '/', '%']  # list: operator string

func = add, sub, mul, div, rem  # tuple: function pointer

a, b = 70, 30
for i in range(5):
    print (f'{i+1}) {a} {op[i]} {b} = {func[i](a, b)}')