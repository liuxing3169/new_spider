# New Spider
新闻抓取工具，使用 Selenium 和 Scripy 进行新闻内容抓取和分析

## Dev setup
cd new_spider
pip install pipenv
pipenv install 

## Run
pipenv run python selenium_spider/qq_news.py && pipenv run  python hot_new.py

or 

pipenv run scrapy runspider scrapy_spider/scrapy_spider/spiders/cnnews_spider.py


## 代码规范检查
pipenv run pylint ./