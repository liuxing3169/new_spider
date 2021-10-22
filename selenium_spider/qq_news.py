"""抓取腾讯新闻的蜘蛛
"""

import os
import logging
import logging.config
import yaml
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
from file_helper import repos_init

    
with open('conf/logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())
logging.config.dictConfig(log_cfg)

news_file_name = "logs/news/qq/" + datetime.now().strftime("%Y%m%d") + ".txt"

def visit_news(news):
    driver = Firefox()
    for new in news:
        # assert len(driver.window_handles) == 1
        logging.debug("begin to visit " + new['href'])
        driver.get(new['href'])
        try:
            new_title = driver.find_element(By.CSS_SELECTOR, "div.qq_conent h1")
            nf = open(news_file_name, 'a')
            nf.write('='*50 + '\n')
            nf.write(new_title.text + '\n')
            nf.write('-'*50 + '\n')
            # logging.info(new_title.text)
            new_body_contents = driver.find_elements(By.CSS_SELECTOR, "div.qq_conent div.content-article p.one-p")
            # breakpoint()
            if new_body_contents:
                for p in new_body_contents:
                    nf.write(p.text + '\n')
                    # logging.info(p.text)
            nf.close()
        except NoSuchElementException as err:
            logging.error(err)

    driver.close()


logging.debug('begin to visit qq news.')
with webdriver.Firefox() as driver:
    repos_init()
    logging.debug('begin to create a news file ' + news_file_name)
    if os.path.exists(news_file_name):
        os.remove(news_file_name)
    Path(news_file_name).touch()
    logging.debug('finished create a news file ' + news_file_name)
    wait = WebDriverWait(driver, 10)
    driver.get("https://news.qq.com/")
    new_list = []
    main_news = driver.find_elements(By.CSS_SELECTOR, "#List ul.list li.item a")
    first_result = wait.until(presence_of_element_located((By.ID, "load-more")))
    for new in main_news:
        if new.text and new.text != '':
            new_list.append({"text": new.text, "href":new.get_attribute('href')})
    side_news = driver.find_elements(By.CSS_SELECTOR, "div#Right ul.list li.item a")
    for new in side_news:
        if new.text and new.text != '':
            new_list.append({"text": new.text, "href":new.get_attribute('href')})
    # print(new_list)
    visit_news(new_list)
logging.debug('finished visit qq news.') 