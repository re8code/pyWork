def info (no, v):
    print (f'{no}) value = {v}')

def delegator (f, no, a):  # delegator: 위임자
    print('>>>>> delegator call')
    f (no, a)

info (1, 10)

# function pointer shallow copy
p = info
p (2, 20); print()

# shallow copy pointer
print (f'3) pointer: {id(p)}, {id(info)}')
print (f'4) pointer: {type(p)}, {type(info)}'); print()

# delegation
delegator (p, 5, 30)
delegator (info, 6, 40)