# -*- coding: utf-8 -*-
import scrapy


class IkyucazspiderSpider(scrapy.Spider):
    name = 'ikyucazSpider'
    allowed_domains = ['www.ikyu.com/caz/00030058/review/']
    start_urls = ['http://www.ikyu.com/caz/00030058/review//']

    def parse(self, response):
        pass
