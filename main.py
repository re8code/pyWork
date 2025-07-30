import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd, hippy.\n\
http://www.naver.com\
"

print(f'1) result      : {re.findall(r'h..p', str)}')
print(f'2) result      : {re.findall(r'https?', str)}')
print(f'3) result      : {re.findall(r'dd*', str)}')
print(f'4) result      : {re.findall(r'b+', str)}')

