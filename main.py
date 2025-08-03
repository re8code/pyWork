import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd, hippy.\n\
http://www.naver.com\
"

# meta character, \d
result = re.findall(r'\w', str)
print(f'1) count: {len(result)}')
print(result, end='\n\n')

result = re.findall(r'[0-9a-zA-Z_]', str)
print(f'2) count: {len(result)}')
print(result)
