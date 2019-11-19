# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProgrammersearchItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.field()
    title = scrapy.Field()
    description = scrapy.Field()
    time = scrapy.Field()
    # pass
