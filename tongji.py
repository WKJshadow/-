import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }

comment = []
comments = []
page = '1613672133105'
cursor = '0'

for i in range(0, 1024):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(page)
    source = requests.get(url, headers=headers).content.decode()
    con='"content":"(.*?)"'
    comment = re.compile(con,re.S).findall(source)
    comments.append(comment)
    id='"last":"(.*?)"'
    cursor = re.compile(id,re.S).findall(source)[0]
    page = str(int(page) + 1)

with open('comments.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(comments, indent=2, ensure_ascii=False))
    print(comments)