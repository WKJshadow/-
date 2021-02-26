import jieba
import re
import json
from collections import Counter
cut_words=""
for line in open('./comments.json',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
print(all_words)
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

print('\n词频统计结果：')
comments = []
for (k,v) in c.most_common(300):# 输出词频最高词
    #print("%s:%d"%(k,v))
    comment = {}
    comment["name"] = k
    comment["value"] = v
    comments.append(comment)
    print(comments)
with open('fenci.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(comments, indent=2, ensure_ascii=False))