# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ProgrammersearchPipeline(object):
    def process_item(self, item, spider):
        with open("my_cnblogs.txt",'a') as fp:
            fp.write(item['name'])
            fp.write(item['content'])
            fp.write(item['time'])
            fp.write(item['link'])
