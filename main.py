import re

str = "010-1234-5678\n\
thesecon@gmail.com\n\
https://www.gildong.com/?p1=1412&p2=alskqwer\n\
The quick brown fox jumps over the lazy dog.\n\
abbcccdddd\
"

pattern = r"the"
res = re.search(pattern, str)

print(f'1) result type : {type(res)}')
print(f'2) result      :', res)
print(f'3) res[0]      :', res[0])
print(f'4) res.group() :', res.group())
print(f'5) res.group(0):', res.group(0))
