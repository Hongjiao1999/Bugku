#1
'''
import requests
import base64

url = 'http://123.206.87.240:8002/web6/'
req = requests.session()
res = req.get(url)
#获取请求头中的flag
flag = res.headers['flag']
#对flag进行base64解码  --- 得到的是bytes类型
txt = base64.b64decode(flag)
#把bytes类型转换成str类型    --- 即对其进行解码 详解请看 https://blog.csdn.net/lanchunhui/article/details/72681978
txt = bytes.decode(txt)
#截取字符串flag后面的字段
txt = txt[txt.index(":")+2:]
#然后再对其进行base64解码
txt = base64.b64decode(txt)
#根据题目提示  now you have to post the margin what you find  --- 需要根据margin属性进行post请求提交
#构造data，另margin属性为爆破出来的txt
data = {'margin': txt}
ans = req.post(url, data)
print(ans.content)
'''

#2
'''
import requests
import base64

url = "http://123.206.87.240:8002/web6/"
r = requests.session()
headers = r.get(url).headers  # 因为flag在消息头里

mid = base64.b64decode(headers['flag'])
mid = mid.decode()  # 为了下一步用split不报错，b64decode后操作的对象是byte类型的字符串，而split函数要用str类型的

flag = base64.b64decode(mid.split(':')[1])  # 获得flag:后的值
data = {'margin': flag}
print(r.post(url, data).text)  # post方法传上去
'''