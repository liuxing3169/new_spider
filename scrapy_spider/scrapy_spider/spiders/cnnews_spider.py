import os
import logging
import logging.config
import yaml
from datetime import datetime
from pathlib import Path
import scrapy

with open('conf/logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())
logging.config.dictConfig(log_cfg)

news_file_name = "logs/news/cnnews/" + datetime.now().strftime("%Y%m%d") + ".txt"


class CNNewsSpider(scrapy.Spider):
    name = "cnnews"

    def start_requests(self):
        # breakpoint()
        if os.path.exists(news_file_name):
            os.remove(news_file_name)
        else:
            try:
                os.mkdir(os.path.dirname(news_file_name))
            except OSError as err:
                logging.error(err)
        with open(news_file_name, 'w') as f:
            f.write("")
        urls = [
            'http://www.news.cn/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # breakpoint()
        for new_href in response.xpath("//div[contains(@class, 'headnews') or contains(@class, 'focus')]//a/@href").getall():
            yield scrapy.Request(new_href, self.parse_new_page)
        # for new_href in response.xpath("//div[contains(@class, 'headnews')]//a/@href").getall():
        #     yield scrapy.Request(new_href, self.parse_new_page)
        # for new_href in response.xpath("//div[contains(@class, 'focus')]//a/@href").getall():
        #     yield scrapy.Request(new_href, self.parse_new_page)
        # for new_href in response.xpath("//div[contains(@class, 'main')]//a/@href").getall():
        #     yield scrapy.Request(new_href, self.parse_new_page)

    def parse_new_page(self, response):
        # breakpoint()
        if response.status == 200:
            nf = open(news_file_name, 'a')
            # nf.write(response.url + '\n')
            nf.write('='*50 + '\n')
            nf.write(response.css("title::text").get() + '\n')
            nf.write('-'*50 + '\n')
            new_body_contents = response.css('div#detail p')
            if new_body_contents:
                for p in new_body_contents:
                    if p.css('::text').get():
                        nf.write(p.css('::text').get() + '\n')
            #         # print(p.get())
            nf.close()