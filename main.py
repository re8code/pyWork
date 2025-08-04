import re

str = "my.domain.com\n\
abcmy.domain.comxyz\n\
www.gildong.com,\n\
www.naver.com\n\
www.naver-1.com\n\
en.kakao.co.kr"

result = re.findall(r'\b\w{2,}\.\w{3,}\.\w{2,}\b', str);         print(f'1) result: {result}')
result = re.findall(r'(\w{2,}\.\w{3,}\.\w{2,})',   str);         print(f'2) result: {result}')
result = re.findall(r'\w{2,}\.\w{3,}\.\w{2,}',     str);         print(f'3) result: {result}')
