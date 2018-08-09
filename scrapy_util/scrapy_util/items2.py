# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Master(scrapy.Item):
    name = scrapy.Field()
    display_name = scrapy.Field()
    tag = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
    thumbnail = scrapy.Field()
    image_url = scrapy.Field()
    volume_url = scrapy.Field()
