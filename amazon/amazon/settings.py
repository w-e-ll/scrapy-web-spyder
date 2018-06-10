# -*- coding: utf-8 -*-

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'amazon_books_db'
MYSQL_USER = 'root'
MYSQL_PASSWD = '9900'

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
HTTPCACHE_ENABLED = True

ITEM_PIPELINES = {
    'amazon.pipelines.AmazonPipeline': 300,
}


