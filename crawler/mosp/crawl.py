import scrapy
from scrapy.crawler import CrawlerProcess
from  mosp.spiders.mo import MoSpider





process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)','LOG_LEVEL':'INFO','ITEM_PIPELINES': {'mosp.pipelines.Pipeline':300},

})

process.crawl(MoSpider)
process.start() # the script will block here until the crawling is finished
