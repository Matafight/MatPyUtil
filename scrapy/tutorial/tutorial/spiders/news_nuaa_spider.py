import scrapy
from tutorial.items import news_nuaa_items
class news_nuaa_spider(scrapy.Spider):
    name = 'news_nuaa_spider'
    start_urls = ['http://cs.nuaa.edu.cn/?p=16230']
    allowed_domains = ['cs.nuaa.edu.cn']
    def parse(self,response):
        item = news_nuaa_items()
        #sles= response.xpath('//div[@class = "content"]')
        news_title = response.xpath('//h2[@class = "C"]/text()')

        for title in news_title:
            tartitle  = title.extract()
            item['title'] = tartitle.encode('utf-8')
            print(item['title'])
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
