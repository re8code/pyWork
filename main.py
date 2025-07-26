s = set()
s.add((1, 2, 3, 4, 5))
s.add('build')
s.add(range(9,0,-2))

idx = 1
for r in s:
    print(f'{idx})', end=' ')
    for c in range(len(r)): print(r[c], end=' ')
    print(type(r))
    idx += 1
s.clear()
print('------------------------------')

l = []
l.append({1, 2, 3, 4, 5})
l.append(set([2, 3, 4, 5, 6]))
l.append({v for v in range(3, 8)})

for r in range(3):
    print(f'{r+1})', end=' ')
    for c in l[r]: print(c, end=' ')
    print(type(l[r]))
