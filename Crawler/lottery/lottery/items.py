# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lottery_date = scrapy.Field()
    issue = scrapy.Field()
    red1 = scrapy.Field()
    red2 = scrapy.Field()
    red3 = scrapy.Field()
    red4 = scrapy.Field()
    red5 = scrapy.Field()
    red6 = scrapy.Field()
    blue1 = scrapy.Field()
    # blue2 = scrapy.Field()
