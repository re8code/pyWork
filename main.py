import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd, hippy.\n\
http://www.naver.com\
"

print(f'1) result      : {re.findall(r'[abc]', str)}')
print(f'2) result      : {re.findall(r'[0-9]', str)}')
print(f'3) result      : {re.findall(r'[a-z]', str)}')
print(f'4) result      : {re.findall(r'[A-Z]', str)}')
print(f'5) result      : {re.findall(r'[0-9A-Z]', str)}')
