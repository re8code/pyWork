import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd\
"

print(f'1) result      : {re.findall(r'^the', str)}')
print(f'2) result      : {re.findall(r'^the', str, re.M)}')
print(f'3) result      : {re.findall(r'^the', str, re.M|re.I)}')
print(f'4) result      : {re.findall(r'com$', str, re.M)}')
print(f'5) result      : {re.findall(r'fox|dog', str)}')
