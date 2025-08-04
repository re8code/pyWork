import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd, hippy.\n\
http://www.naver.com\
"

result = re.findall(r'(bb|ww|\/\/)', str)
print(f'1) result: {result}')

result = re.findall(r'\b\w{2,}\.\w{3,}\.\w{2,}\b', str)
print(f'2) result: {result}')
