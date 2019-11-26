import requests

url = 'http://117.51.158.44/app/Session.php'
headers = {
    'User-Agent': 'Mozilla',
    'didictf-username': 'admin',
}
r = requests.post(url=url, headers=headers)
print(r.cookies)    #返回的cookie需要url解码
