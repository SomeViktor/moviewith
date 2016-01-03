# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from mosp.items import *
import re
import sys

#from scrapy.utils.project import get_project_settings


class MoSpider(scrapy.Spider):
	name = "mo"
	allowed_domains = ["wikipedia.org"]
	
	start_urls = [
		#'https://en.wikipedia.org/wiki/Category:1998_films',
		#'https://en.wikipedia.org/wiki/Category:1999_films'
	]

	for x in range(24):
		y = x + 1990
		start_urls.append("https://en.wikipedia.org/wiki/Category:"+ str(y)+"_films")

	print start_urls


	

	def parse(self, response):
		#all the categories on the page
		movies_parsed = 0;
		mwcategorygroups = response.selector.xpath('//div[@class="mw-category-group"]')
		#print mwcategorygroups
		#now lets find which ones have a h3 from 1-9,A-Z.
		sys.stdout.write("--------\nletters:")
		u = re.compile("([A-Z,1-9])")
		for cat in mwcategorygroups:
			h3 = cat.xpath('h3/text()').extract();
			h = h3[0].encode('utf-8');
			
			if u.match(str(h)):
				sys.stdout.write(str(h));
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
					movies_parsed += 1;



					yield movie_request;



				sys.stdout.write(":"+ str(movies_parsed) + ",  ")
			
				

		sys.stdout.write("\n")
		next_link = "";
		nlt = response.selector.xpath('/html/body/div[3]/div[3]/div[4]/div[5]/div[2]/a[2]/text()').extract();
		#print nlt[0]
		if nlt[0] == "next page":
			next_link = response.selector.xpath('/html/body/div[3]/div[3]/div[4]/div[5]/div[2]/a[2]/@href').extract();

		if len(next_link) == 0:
			print "no next link anymore, year is finished."
			return
			
		else:
			next_url = "https://en.wikipedia.org" + next_link[0];
			#print "next url: " + next_url
			yield scrapy.Request(next_url);


	def parse_movie(self,response):
		#print "got a request to parse, url: " + response.request.url
		movie = Movie();
		
		better_title = response.selector.xpath('//*[contains(@class , "infobox")]/tr/th/text()').extract();

		if len(better_title) == 0:
			#print "no infobox:"
			#print response.request.url
			#print "movie dropped"
			return
			#print response.selector.xpath('//*[contains(@class , "infobox")]').extract();
		else:
			#print better_title[0], "\n\n";
			movie['title'] = better_title[0];


		#print better_title;
		
		#first: find starring row.
		actors_list = []
		starring_line = ""
		rows = response.selector.xpath('//*[contains(@class , "infobox")]/tr')
		for row in rows:
			line = row.xpath('th/text()').extract();
			if len(line) > 0:
				if line[0] == "Starring":
					actors = row.xpath('td/a/text()').extract();
					if len(actors) == 0:
						actors = row.xpath('td/div/ul/li/text()').extract();
					if len(actors) == 0:
						actors = row.xpath('td/text()').extract();
					for actor in actors:
						#print actor
						actors_list.append(actor)
		movie['actors'] = actors_list
		#print len(actors_list)
		if len(actors_list) > 0:
			return movie;
		else:
			
			for row in rows:
				line = row.xpath('th/text()').extract();
				#print len(line)
				if len(line) > 0:
					#print line[0];
					
					
					if line[0] == "Starring":
						print "-------------------debug info:---------------"
						print "no actors",response.request.url
						print row.xpath('td').extract();
						print "------------------------------------------\n"