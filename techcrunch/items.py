# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TechcrunchItem(scrapy.Item):
    # define the items
    id = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    datetime = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    blurb = scrapy.Field()
    img = scrapy.Field()
