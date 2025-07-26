import array as ar

d = {}

# Available as Dictionary Key
# : integer, float, tuple, string, range, generator, map

d[0] = 1                              # integer
d[1.0] = 2                            # float
# d[true] = 'error'                   # boolean     (X)
# d[[1,2]] = 'error'                  # list        (X)
d[2,] = 3                             # tuple
d['str'] = 4                          # string
# d[ar.array('i', [1, 2])] = 'error'  # array       (X)
# d[{1:'a', 2:'b'}] = 'error'         # dictionary  (X)
d[range(2)] = 5                       # range
# d[{1,2}] = 'error'                  # set         (X)
d[(i for i in range(2))] = 6          # generator
d[map(int, [1,2])] = 7                # map

idx = 1
for k in d.keys():
    print(f'{idx}) key type: {type(k)}')
    idx += 1
