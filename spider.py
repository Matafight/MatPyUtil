#_*_ coding:utf-8 _*_
import urllib2
import urllib
import cookielib
import re
#cookie = cookielib.CookieJar()
#handler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handler)
#response  = opener.open("http://www.baidu.com")

#for item in cookie:
    #print 'Name = ' + item.name
    #print 'Value = ' + item.value
#
#save cookie to files

#filename = 'cookie.txt'
#cookie = cookielib.MozillaCookieJar(filename)
#handler = urllib2.HTTPCookieProcessor(cookie)
#openor = urllib2.build_opener(handler)
#resonse = openor.open('http://www.baidu.com')
#cookie.save(ignore_discard = True,ignore_expires = True)

##get cookier from file and then visit the website

#filename = 'cookie.txt'
#cookie = cooklib.MozillaCookieJar()
#cookie.load('cookie.txt',ignore_discard = True,ignore_expires = True)
#openor = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#request = urllib2.request('http://www.baidu.com')
#response = openor.open(request)

page = 1
url = 'http://www.qiushibaike.com/8hr/page/3/?s=4909604'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)

content = response.read().decode('utf-8')
pattern=re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>(.*?)<div class="stats".*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash".*?i class="number">(.*?)</i>(.*?)</a>',re.S)
items = re.findall(pattern,content)
picpatt = re.compile('img')
#picres = re.findall(picpatt,items[2])
#print(len(picres))
#if(len(picres) ==0):

tofile = open('jiushibaike.txt','w')

for item in items:
    picres = re.search(picpatt,item[2])
    if(not picres):
        print item[1]

        tofile.writelines(item[1].encode('utf-8'))
