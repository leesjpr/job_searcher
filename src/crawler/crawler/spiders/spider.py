import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

import pprint

start_urls = [] 

class CoreSpider(scrapy.Spider):
    # crawler name
    name = "core"

    # site domain
    allowed_domains = ['http://www.redcross.or.kr/']

    # site urls
    start_urls = [
        'http://www.redcross.or.kr/education_safety/education_safety_rescueagent.do?action=eduApply'
    ]


    def parse(self, response):
        filename = response.url.split("/")[-2]

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)

        #urls = response.css('a').xpath('@href').extract()
        last_page_url = response.xpath('//*[@id="area_section"]/div[8]/ul/li[8]/a').extract()
        self.log(pprint.pprint(last_page_url))
        
        each_urls = response.xpath('//*[@id="area_section"]/div[7]/table/tbody/tr[*]/td[3]/a/@href').extract()

        self.log(pprint.pprint(each_urls))
