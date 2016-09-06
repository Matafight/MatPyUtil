import scrapy
import re
from tutorial.items import news_nuaa_items
class news_nuaa_spider(scrapy.Spider):
    name = 'news_nuaa_spider'
    start_urls = ['http://cs.nuaa.edu.cn/?cat=12&paged=1']

    allowed_domains = ['cs.nuaa.edu.cn']
    def parse(self,response):

        for page in range(1,10,1):
            urls = 'http://cs.nuaa.edu.cn/?cat=12&paged='+str(page)
            yield scrapy.Request(urls,callback = self.parse_urls)


    def parse_urls(self,response):
        exp = re.compile(r'<td\s+height="20"><a\s+href="(.*?)">')

        resphtml = re.findall(exp,response.body)

        for links in resphtml:
            print(links)
            yield scrapy.Request(links,callback = self.parse_items)
    def parse_items(self,response):
        item = news_nuaa_items()

        #sles= response.xpath('//div[@class = "content"]')
        news_title = response.xpath('//h2[@class = "C"]/text()')

        for title in news_title:
            tartitle  = title.extract()
            item['title'] = tartitle.encode('utf-8')
            #print(item['title'])
        news_time = response.xpath('//div[@class= "info"]/text()')

        for time in news_time:
            tartime = time.extract().encode('utf-8')
            item['time']= tartime

        news_content = response.xpath('//div[@class= "content"]')

        main_content = ""
        for content in news_content:
            para = content.xpath('p/text()')

            for para2 in para:
                if (para2 == None):
                    pass
                else:
                    duanluo = para2.extract().encode('utf-8')
                    main_content = main_content + duanluo
        item['content']= main_content
        yield item
        #for sele in sles:
        #    pagarph = sele.xpath('p/text()')
        #    for links in pagarph:
        #    #    link = links.xpath('@href')
        #        print(links.extract().encode('utf-8'))
        #        print("temp")
        #    #    print(links.extract())
        #print(item['news_content'][0])
        #yield item
        #pass
