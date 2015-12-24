# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#models for moviewebsite
class Movie(scrapy.Item):
 	title = scrapy.Field();
 	director = scrapy.Field();
 	release_year = scrapy.Field();
 	#and some set with actors. Maybe a string? => manual


