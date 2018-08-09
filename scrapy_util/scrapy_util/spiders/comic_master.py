# -*- coding: utf-8 -*-
import scrapy
from ..items2 import Master
import re
import os
from urlparse import urljoin

project_dir = os.path.abspath(os.path.dirname(__file__))

class ComicMasterSpider(scrapy.Spider):
    name = 'gtsb'
    begin_url = "http://comic.kukudm.com/comiclist/21/index.htm"
    #log_file = '/var/myproject/comic/scrapy_util/' + name + '.log'
    custom_settings = {
        'IMAGES_URLS_FIELD' :"image_url",
        'IMAGES_STORE':os.path.join(project_dir,'images'),
        'IMAGES_EXPIRES': 90,
    #'FEED_EXPORT_ENCIDING':'utf-8',
        'ITEM_PIPELINES':{
        'scrapy_util.scrapy_util.pipelines2.MasterPipeline': 300, 
        },
    #    'LOG_FILE':log_file,
    }

    def start_requests(self):
        yield scrapy.Request(self.begin_url, self.get_volume)

    def get_volume(self, response):
        current_page = 0
        volume_href = response.css("#comiclistn > dd > a:nth-child(1)::attr('href')").extract()
        volume_name = response.css("#comiclistn > dd > a:nth-child(1)::text").extract()
        volumes = zip(volume_href, volume_name)
        volume_num = 0
        item = Master()
        item['name'] = self.name
        item['display_name'] = response.xpath("/html/body/table[5]/tr/td[2]/table/tr[1]/td/table/tr[1]/td/text()").extract()[0]
        item['tag'] = 'funny'
        detail = response.xpath("/html/body/table[5]/tr/td[2]/table/tr[1]/td/table/tr[5]/td/text()").extract()[0].split('|')
        item['author'] = detail[0]
        img_url = response.css('td > table > tr:nth-child(2) > td > img::attr(src)').extract()
        item['image_url'] = img_url
        item['summary'] = response.css("#ComicInfo::text").extract()[0]
        #if check_repeating(self.name):
        #    return
        for each in volumes:
            volume_num = volume_num + 1
            gallery = urljoin("http://comic.kukudm.com/", each[0])
            item['volume_url'] = gallery
            yield item
            #request = scrapy.Request(gallery, callback = self.parse)
            #request.meta['volume_name'] = each[1]
            #request.meta['volume'] = volume_num
            #request.meta['current_page'] = current_page
            #yield request

    @staticmethod
    def close(spider, reason):
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)


from scrapy.crawler import CrawlerProcess

def start_scrapy():
    process = CrawlerProcess()
    process.crawl(ComicMasterSpider)
    process.start() 
