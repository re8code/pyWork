import array as ar

def info(no):
    global s; print(f'{no}) set data:', s)

s = set()

s.add(1);   info(1)                    # integer
s.add(2.3); info(2)                    # float
# s.add(true)                          # bool       (X)
# s.add([1, 2])                        # list       (X)
s.add((1,2)); info(3)                  # tuple
s.add('str'); info(4)                  # string
# s.add(ar.array('i', [1, 2]))         # array      (X)
# s.add({1:'a', 2:'b'})                # dictionary (X)
s.add(range(2)); info(5)               # range
# s.add({1,2})                         # set        (X)
s.add((i for i in range(2))); info(6)  # generator
s.add(map(int, [1, 2])); info(7)       # map
print()

index = 1
for v in s:
    print(f'{index}) type:', type(v)); index += 1
