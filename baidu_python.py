# -*- coding: cp936 -*-
import urllib
import urllib2
import requests
import re
import sys  #引入模块
from datetime import date,datetime
from bs4 import BeautifulSoup

list_tokens=[]
list_urls=[]

def getBdUrl(test,page):
        url_path="https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=ab9b7e4d0002be05&"
        url_wd="wd="+test
        url_page="&pn="+str(page)+"&"
        url_oq="oq="+test
        url_only="&&tn=monline_4_dg&ie=utf-8&rsv_pq=ab9b7e4d0002be05&"
        url_token="rsv_t=493bkfnoBh1RpB9T3ivEnfFbIg0Z7qGVREHow04J9J3CnIc3ZB1Ff3WMgYccelEhSk3a"
        url_bs="&bs="+test
        url_footer="&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=13&_cr1=29155"
        get_url=url_path+url_wd+url_page+url_oq+url_only+url_token+url_bs+url_footer

        cookie = '''BAIDUID=AD70535454203309B98B62FF92448EDE:FG=1; BIDUPSID=AFB669C168B2C0DE896F795BB769185F; PSTM=1541381323; BDUSS=Z5QXhsfnBLUVJoTC1TN2toVnV1VjlkZDNOSXNKNEZSOXQ5M2FjZE51VlNTMXBjQUFBQUFBJCQAAAAAAAAAAAEAAABnlldjxOO~tL-0tPPNvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFK-MlxSvjJcUH; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=7; H_PS_PSSID=1455_21094_28608_28584_28558_28519_28626_22157; pgv_pvi=265141248; pgv_si=s1405583360; cflag=13%3A3; sugstore=0; H_PS_645EC=493bkfnoBh1RpB9T3ivEnfFbIg0Z7qGVREHow04J9J3CnIc3ZB1Ff3WMgYccelEhSk3a; BDSVRTM=115'''
        header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'is_referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_4_dg&wd=%E6%94%BF%E5%BA%9C%20intitle%3A%E4%B8%AD%E5%9B%BD&oq=%25E6%2594%25BF%25E5%25BA%259C%2520intitle%253A%25E4%25B8%25AD%25E5%259B%25BD&rsv_pq=c68600120002bfe8&rsv_t=b831%2BJwOrS%2BLBuDN7zNBw475uOnFDIihHJASJpZEuc8ixvKchtYmvLhX5bE4kjCHl8%2F6&rqlang=cn&rsv_enter=0&bs=%E6%94%BF%E5%BA%9C%20intitle%3A%E4%B8%AD%E5%9B%BD',
        'is_xhr': '1',
        'is_pbs': '%E6%94%BF%E5%BA%9C%20intitle%3A%E4%B8%AD%E5%9B%BD',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.baidu.com/s?wd=%E6%94%BF%E5%BA%9C%20intitle%3A%E4%B8%AD%E5%9B%BD&pn=10&oq=%E6%94%BF%E5%BA%9C%20intitle%3A%E4%B8%AD%E5%9B%BD&tn=monline_4_dg&ie=utf-8&rsv_pq=ab9b7e4d0002be05&rsv_t=333fjYDiK5Z76BD3NAi4oxd1XoCaUHNuxKSx9%2B1wPEyTZCPz0E8dyf%2BHgabh2r8qUVCc',
        'Cookie': cookie}
        
        wbdata = requests.get(get_url,headers=header).text
        soup = BeautifulSoup(wbdata,'html5lib')
        html_strs = soup.prettify()
        html_strs=re.sub(' ', '',html_strs)
        html_strs=re.sub('\n', '',html_strs)
        html_list=html_strs.split('<divid="content_left">')
        html_list=html_list[1].split('<divstyle="clear:both;height:0;">')
        html_list=html_list[0].split('"href="http://www.baidu.com/link?url=')
        html_list.remove(html_list[0])
        
        for x in html_list:
                html_list=x.split('"')
                list_tokens.append('http://www.baidu.com/link?url='+html_list[0])


def getUrl(token_url):

        cookie = '''BAIDUID=AD70535454203309B98B62FF92448EDE:FG=1; BIDUPSID=AFB669C168B2C0DE896F795BB769185F; PSTM=1541381323; BDUSS=Z5QXhsfnBLUVJoTC1TN2toVnV1VjlkZDNOSXNKNEZSOXQ5M2FjZE51VlNTMXBjQUFBQUFBJCQAAAAAAAAAAAEAAABnlldjxOO~tL-0tPPNvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFK-MlxSvjJcUH; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1455_21094_28608_28584_28558_28519_28626_22157; H_PS_645EC=db7b1HRVO%2BvW8d2C%2Fe%2BBaf2n5G23WzREUKkCe3na655U1OZ1fK0lhN5DN95WEpb8iyLI; sugstore=0; delPer=0; BD_CK_SAM=1; PSINO=7; pgv_pvi=5688612864; pgv_si=s7858489344; BDSVRTM=0; locale=zh'''
        header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': cookie}
        
        res = requests.get(url=token_url, headers=header, allow_redirects=False)
        return res.headers['location']
        

if __name__ == '__main__':
        
        sun=int(sys.argv[2])
        s_test=sys.argv[1]
        str1 =urllib.unquote(s_test)
        
        print '搜索字符：',str1.decode('utf-8')
        print '爬取',sun,'页'
                
        for a in range(sun):
                getBdUrl(s_test,a*10)


        list_tokens = list(set(list_tokens))
        print len(list_tokens)
        for i in list_tokens:
                list_urls.append(getUrl(i))

        f=open('url.txt','w')
        for x in list_urls:
                f.write(x)
                f.write('\n')
        f.close()
                

        
        




