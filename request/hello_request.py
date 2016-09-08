#_*_ coding:utf-8 _*_
import requests
import pickle

from cookielib import LWPCookieJar

def login_save_cookies():
    #使用post登陆教务处
    s = requests.Session()

    s.cookies = LWPCookieJar('COOKIES')
    url = 'http://gsmis.nuaa.edu.cn/nuaapyxx/login.aspx'
    data = {'__VIEWSTATE':'dDwyMTQxMjc4NDIxOztsPF9jdGwwOkltYWdlQnV0dG9uMTtfY3RsMDpJbWFnZUJ1dHRvbjI7Pj6npam+xCYtLIbC71L7AOB8nX3tPQ=='
    ,'_ctl0:txtusername':'',
    '_ctl0:txtpassword':'a'
    ,'_ctl0:ImageButton1.x':21
    ,'_ctl0:ImageButton1.y':15}
    res = s.post(url,data = data)
    print(res.text)
    #ignore_discard 意思是即使cookie将要被丢弃也要保存下来，一定要设置为True，不然就不会保存了
    s.cookies.save(ignore_discard = True)




def login_with_cookies():
    s = requests.Session()
    s.cookies = LWPCookieJar('COOKIES')

    url = 'http://gsmis.nuaa.edu.cn/nuaapyxx/Default.aspx'
    s.cookies.load(ignore_discard = True)
    res = s.get(url)
    print(res.text)


if __name__=="__main__":
    #login_save_cookies()
    login_with_cookies()
