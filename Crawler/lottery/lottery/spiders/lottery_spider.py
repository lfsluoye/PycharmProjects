# -*- coding: utf-8 -*-
import scrapy
from lottery.items import LotteryItem


class LotterySpiderSpider(scrapy.Spider):
    name = 'lottery_spider'
    allowed_domains = ['kaijiang.zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']
    def parse(self, response):
        print(response)
        lottery_list = response.xpath("//table[@class='wqhgt']/tr")
        i = 0
        for i_item in lottery_list:
            i += 1
            if i == 1 or i == 2 or i == len(lottery_list):
                continue
            lottery_item = LotteryItem()
            lottery_item['lottery_date'] = i_item.xpath("./td[1]/text()").extract_first()
            lottery_item['issue'] = i_item.xpath("./td[2]/text()").extract_first()
            lottery_item['red1'] = i_item.xpath("./td[3]/em[1]/text()").extract_first()
            lottery_item['red2'] = i_item.xpath("./td[3]/em[2]/text()").extract_first()
            lottery_item['red3'] = i_item.xpath("./td[3]/em[3]/text()").extract_first()
            lottery_item['red4'] = i_item.xpath("./td[3]/em[4]/text()").extract_first()
            lottery_item['red5'] = i_item.xpath("./td[3]/em[5]/text()").extract_first()
            lottery_item['red6'] = i_item.xpath("./td[3]/em[6]/text()").extract_first()
            lottery_item['blue1'] = i_item.xpath("./td[3]/em[7]/text()").extract_first()
            yield lottery_item
        next_link= response.xpath("//p[@class='pg']/strong[5]/a/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://kaijiang.zhcw.com" + next_link, callback=self.parse)
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)




