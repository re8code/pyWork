s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

# 교집합
result = s1 & s2;                     print('1) s1 & s2 =', result)
result = s1.intersection(s2);         print('2) s1 & s2 =', result)
print()

# 합집합
result = s1 | s2;                     print('3) s1 | s2 =', result)
result = s1.union(s2);                print('4) s1 | s2 =', result)
print()

# 차집합
result = s1 - s2;                     print('5) s1 - s2 =', result)
result = s1.difference(s2);           print('6) s1 - s2 =', result)
print()

# 대칭차집합 = 합집합 - 교집합
result = s1 ^ s2;                     print('7) s1 ^ s2 =', result)
result = s1.symmetric_difference(s2); print('8) s1 ^ s2 =', result)
resunt = s1 | s2 - s1 & s2;           print('9) s1 ^ s2 =', result)
