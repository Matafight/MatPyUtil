import urllib2
import urllib
import cookielib

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

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
print(response.read())


content = response.read().decode('utf-8')
pattern=re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats".*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash".*?i class="number">(.*?)</i>(.*?)</a>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item [1] ,item [2] ,item [3] ,item [4] ,item [5] 　
