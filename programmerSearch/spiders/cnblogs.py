# -*- coding: utf-8 -*-
import scrapy
from programmerSearch.items import ProgrammersearchItem
from pyquery import PyQuery as pyq
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://cnblogs.com/']

    def parse(self, response):
        body = scrapy.Selector(text=response.body)
        posts = body.xpath('//div[@class="el-card post"]')
        post = posts[0]
        links = post.xpath('//a[@class="title"]/@href').extract()
        titles = post.xpath('//a[@class="title"]/text()').extract()
        descriptions = post.xpath(
            '//div[@class="description"]/text()').extract()
        for i in range(len(posts)):
                post_item = {}
                post_item['link'] = links[i].encode('utf-8')
                post_item['title'] = titles[i].encode('utf-8').strip()
                post_item['description'] = descriptions[i].encode('utf-8').strip()
                yield item
