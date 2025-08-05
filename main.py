import re

str = "https://www.example.com과 http://company.net 웹사이트를 방문해 주세요. 문의사항은 010-1234-5678\
 또는 02-9876-5432로 전화 주시거나, contact@example.com이나 support@company.net으로 이메일을 보내주시면\
 됩니다."

result = re.findall(r'https?://[0-9a-zA-Z.]+', str)
print(f'1) web URL  : {result}')

result = re.findall(r'\d{2,4}-\d{4}-\d{4}', str)
print(f'2) phone num: {result}')

result = re.findall(r'[a-z]+@[a-z]+.[a-z]+', str)
print(f'3) email add: {result}')
