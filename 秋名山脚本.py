#1
'''
import requests
import re

url = 'http://123.206.87.240:8002/qiumingshan/'
r = requests.session()
requestpage = r.get(url)
ans = re.findall('<div>(.*?)=?;</div>',requestpage.text)#获取表达式
ans = "".join(ans)#列表转为字符串
ans = ans[:-2]#去掉最后的=?
post = eval(ans)#计算表达式的值
data = {'value':post}#构造post的data部分
flag = r.post(url, data=data)
print(flag.text)
'''


#2
'''
import re
import requests

s = requests.Session()
r = s.get("http://123.206.87.240:8002/qiumingshan/")
searchObj = re.search(r'^<div>(.*)=\?;</div>$', r.text, re.M | re.S)
d = {
    "value": eval(searchObj.group(1))
}
r = s.post("http://123.206.87.240:8002/qiumingshan/", data=d)
print(r.text)
'''

#3
'''
import re
import requests

while (True):
    s = requests.Session()
    r = s.get("http://123.206.87.240:8002/qiumingshan/")

    searchObj = re.search(r'^<div>(.*)=\?;</div>$', r.text, re.M | re.S)
    d = {"value": eval(searchObj.group(1))}
    r = s.post("http://123.206.87.240:8002/qiumingshan/", data=d)

    print(r.text)

    if r.text.strip():
        break
'''
