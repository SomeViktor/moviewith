# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from ec.items import *
import copy

class KinoSpider(scrapy.Spider):
    name = "movies"
    start_urls = (
        'https://en.wikipedia.org/wiki/Category:1997_films',
    )

    def parse(self, response):
        #all the categories on the page
        mwcategorygroups = response.selector.xpath('//ul[@class="mw-category-group"]')
        print mwcategorygroups
        #now lets find which ones have a h3 from 1-9,A-Z.
        for cat in mwcategorygroups:
            h3 = cat.xpath('h3/text()');
            print h3


            