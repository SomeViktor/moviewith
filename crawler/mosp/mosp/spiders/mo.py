# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from mosp.items import *
import re

class MoSpider(scrapy.Spider):
    name = "mo"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        'https://en.wikipedia.org/wiki/Category:1997_films',
    ]

    def parse(self, response):
        #all the categories on the page
        
        mwcategorygroups = response.selector.xpath('//div[@class="mw-category-group"]')
        #print mwcategorygroups
        #now lets find which ones have a h3 from 1-9,A-Z.
        u = re.compile("([A-Z,1-9])")
        for cat in mwcategorygroups:
            h3 = cat.xpath('h3/text()').extract();
            h = h3[0].encode('utf-8');
            print str(h)
            if u.match(str(h)):
            	print "matched!"
            	links = cat.xpath('ul/li/a');
            	#print links
            	for link in links:
            		rel_address = link.xpath('@href').extract();
            		name = link.xpath('text()').extract();
            		#print "name: " + name[0];
 	            	#print "link: " + rel_address[0];
	            	movie_request = scrapy.Request("https://en.wikipedia.org" + rel_address[0],  callback=self.parse_movie);
	            	#the titile with this way sometimes has the year in it:
	            	#movie_request.meta['title'] = name[0];
	            	yield movie_request;

            else:
            	print "not our category!"
        next_link = response.selector.xpath('/html/body/div[3]/div[3]/div[4]/div[5]/div[2]/a[2]/@href').extract();
        print "next link:"
        
        
        

        if len(next_link) == 0:
        	print "no next link anymore!"
        	return
        	
       	else:
       		next_url = "https://en.wikipedia.org" + next_link[0];
        	print "next url: " + next_url
        	#yield scrapy.Request(next_url);


    def parse_movie(self,response):
    	print "got a request to parse, url: " + response.request.url
    	movie = Movie();
    	
    	#/html/body/div[3]/div[3]/div[4]/table[1]/tbody/tr[1]/th
    	better_title = response.selector.xpath('/html/body/div[3]/div[3]/div[4]/table[1]/tr/th/text()').extract();
    	if len(better_title) == 0:
    		print "strange case!!!"
    		print response.selector.xpath('/html/body/div[3]/div[3]/div[4]/table[1]/tr').extract();
    	#print better_title;
    	movie['title'] = better_title;
    	print ""
    	print ""
    	actors = response.selector.xpath('/html/body/div[3]/div[3]/div[4]/table[1]/tr[4]/td/text()').extract();
    	if len(actors) == 0:
    		print "movie has no actors, drop movie";
    		return
    	else:
    		for actor in actors:
    			print actor;
    	#fill the item!