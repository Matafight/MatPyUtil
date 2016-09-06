# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TutorialPipeline(object):

    def process_item(self, item, spider):
        return item

class news_nuaa_pipeline(object):
    def __init__(self):
        self.file = open('nuaa_news.txt',mode = 'w')
    def process_item(self,item,spider):
        self.file.write(item['title'])
        print(item['title'])
        self.file.write('\n')
        self.file.write(item['time'])
        self.file.write('\n')
        self.file.write(item['content'])
        self.file.write('\n')
        return item
