# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient


class Pipeline(object):
	def __init__(self):
		client = MongoClient()
		self.mo = client['mo']
		self.mo.movies.drop();
	def process_item(self, item, spider):
		
		movie = dict(item)

		#print "#######################"
		#print item['title']
		result = self.mo.movies.insert(movie)
		#print result
		#print "------------------------\n"
		return item
