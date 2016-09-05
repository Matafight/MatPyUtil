import scrapy

class news_nuaa_spider(scrapy.Spider):
    name = 'news_nuaa_spider'
    start_urls = ['http://cs.nuaa.edu.cn/?cat=12']
    allowed_domains = ['cs.nuaa.edu.cn']
    def parse(self,response):
        pass
