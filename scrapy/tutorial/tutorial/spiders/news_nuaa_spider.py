import scrapy
from tutorial.items import TutorialItem
class news_nuaa_spider(scrapy.Spider):
    name = 'news_nuaa_spider'
    start_urls = ['http://cs.nuaa.edu.cn/?p=16230']
    allowed_domains = ['cs.nuaa.edu.cn']
    def parse(self,response):
        item = TutorialItem()
        sles= response.xpath('//div[@class = "content"]')
        for sele in sles:
            pagarph = sele.xpath('p/text()').extract()
            print(pagarph)
        #print(item['news_content'][0])
        yield item
        #pass
