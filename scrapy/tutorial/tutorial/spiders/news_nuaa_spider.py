import scrapy
from tutorial.items import TutorialItem
class news_nuaa_spider(scrapy.Spider):
    name = 'news_nuaa_spider'
    start_urls = ['http://cs.nuaa.edu.cn/?p=16230']
    allowed_domains = ['cs.nuaa.edu.cn']
    def parse(self,response):
        item = TutorialItem()
        item['news_content'] = response.xpath('//h2[@class = "C"]').extract()
        #print(item['news_content'][0])
        yield item
        #pass
