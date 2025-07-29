import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd\
"

pattern = r"the"
res = re.findall(pattern, str, re.I)

print(f'1) result type : {type(res)}')
print(f'2) result size : {len(res)}')
print(f'3) result      : {res}')
