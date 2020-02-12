"""
爬取vmgirls.com图片，存入数据库
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
res = requests.get('https://vmgirls.com',headers=headers)
print(res.status_code)
# print(res.request.headers)
html = res.text
print(html)