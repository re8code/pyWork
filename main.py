data = '0 1 2 3 4'
print(f'1) {type(data)} :', data)

s = data.split()
print(f'2) {type(s)}:', s)

s = map(int, s)
print(f'3) {type(s)} :', s, ', sum:', sum(s))

s = list(s)
print(f'4) {type(s)}:',  s, ', sum:', sum(s))

s = map(lambda x: int(x)+1, data.split())
l = list(s)
print(f'5) {type(s)} :', s, ', sum:', sum(s))
print(f'6) {type(l)}:',  l, ', sum:', sum(l))