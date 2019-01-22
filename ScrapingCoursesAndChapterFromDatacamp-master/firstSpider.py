# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 02:24:54 2017

@author: H.J. Jia
"""


# use Selector

from scrapy import Selector

import requests

url = 'https://www.datacamp.com/courses/all'

html = requests.get(url).content

sel = Selector(text = html)


course_divs = sel.css('div.course-block')





# use response

import scrapy

from scrapy.crawler import CrawlerProcess

class firstSpider(scrapy.Spider):
    name = 'first_spider'

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    def parse(self, response):
        # write to newfile.html
#        html_file = 'newfile.html'      
#        with open( html_file, 'wb') as f:
#            f.write(response.body)
        
        course_blocks = response.css('div.course-block')
        course_link = course_blocks.xpath('./a/@href')
        links_to_follow = course_link.extract()
        for url in links_to_follow:
            yield response.follow(url = url, callback = self.parse2)
        
            
    def parse2(self, response):
        crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
        crs_title_ext = crs_title.extract_first().strip()
        
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
                         
        yield { crs_title_ext: ch_titles_ext}
        
#        file = 'newfile.csv'      
#        with open( file, 'wb') as f:
#            f.write(dc_dict)
#        
        

#scrapy runspider firstSpider.py -o newfile.json

#process = CrawlerProcess()
#process.crawl(firstSpider)
#process.start()
#            




