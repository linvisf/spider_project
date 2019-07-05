# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PicItem(scrapy.Item):
    """     图片爬取    """
    cname = scrapy.Field()  # 分类名称
    name = scrapy.Field()
    img_url = scrapy.Field()
