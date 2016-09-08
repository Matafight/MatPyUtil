import requests

from cookielib import LWPCookieJar

def login_save_cookies():
        s = requests.Session()
        s.cookies = LWPCookieJar('douban_cookies')
        
