#_*_ coding:utf-8 _*_
import requests
import re
from cookielib import LWPCookieJar
from bs4 import BeautifulSoup
from StringIO import StringIO
import urllib2
from PIL import Image

def login_save_cookies():
        s = requests.Session()
        s.cookies = LWPCookieJar('douban_cookies')

        url = 'https://www.douban.com/accounts/login'
        #用BeautifulSoup 解析登录页面获取验证码
        res = requests.get(url)
        #print(res.text.encode('utf-8'))

        soup = BeautifulSoup(res.text)
        image_url = soup.find(attrs = {'id':'captcha_image'})['src']
        captcha_id = soup.find(attrs = {'name':'captcha-id'})['value']
        print(image_url)

        r = requests.get(image_url)
            #print(r.content)
        ima = Image.open(StringIO(r.content))
        ima.show()
        captcha_solution = raw_input('Captacha are :')
        data = dict([])
        data['source'] = 'None'
        data['redir'] = 'https://www.douban.com'
        data['form_email'] = '1149567097@qq.com'
        data['form_password'] = 'XXX'
        data['captcha-solution'] = captcha_solution
        data['captcha-id'] = captcha_id

        data['login'] = '登录'
        print(data)

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

        res2 = s.post(url,data = data,headers = headers)
        #print(res.content)
        judge_if_log = u'登录豆瓣'

        ret = re.search(re.compile(judge_if_log),res2.text)
        if ret == None:
            print('you have logged in to douban')
        else:
            print('not log yet')

if __name__ == "__main__":
    login_save_cookies()
