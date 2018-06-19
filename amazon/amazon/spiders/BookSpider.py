# -*- coding: utf-8 -*-
import os
import logging

from urllib.request import urlretrieve

from scrapy.utils.log import configure_logging
from scrapy import Spider
from scrapy.http import Request

from amazon.items import *

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()


class BookSpider(Spider):
    image_count = 1
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = [
        'https://www.amazon.com/s/ref=sr_pg_1?rh=n%3A283155%2Cn%3A%211000%2Cn%3A5%2Cn%3A3952%2Cn%3A285856&ie=UTF8&qid'
        '=1526340166',
        'https://www.amazon.com/s/ref=lp_285856_pg_2?rh=n%3A283155%2Cn%3A%211000%2Cn%3A5%2Cn%3A3952%2Cn%3A285856&page'
        '=2&ie=UTF8&qid=1526225464 '
    ]

    def parse(self, response):
        books = response.xpath(
            '//a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//span[@class="pagnLink"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        """
        Amazon Book Spider Crawler TitLe.
        """
        try:
            item = Book()
            pwd = os.getcwd() + '/'

            if not os.path.isdir(pwd + 'crawlImages/'):
                os.mkdir(pwd + 'crawlImages/')
            title = response.xpath('//div[@class="feature"]/div/h1/span/text()').extract()
            if title[0] is None:
                item['Title'] = 'No title added' + ' || ' + str(title).strip()
            elif title[1] is None:
                item['Title'] = title[0] + ' || ' + 'No kindle_title added'
            if len(title) >= 3:
                item['Title'] = str(title[0]).strip() + ' || ' + str(title[1]).strip() + ' | ' + str(title[2]).strip()
            else:
                item['Title'] = str(title[0]).strip() + ' || ' + str(title[1]).strip()

            description = response.xpath('//div[@id="bookDescription_feature_div"]//div/p/text()').extract_first()
            item['Description'] = str(description).strip()

            author = response.xpath('//span[@class="author notFaded"]//span/a[@class="a-link-normal contributorNameID"]/text()').extract_first()
            if author is None:
                item['Author'] = 'No author added'
            else:
                item['Author'] = str(author).strip()

            reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first()
            if reviews is None:
                item['Reviews'] = 'No reviews added'
            else:
                reviews = reviews.replace(" customer reviews", "")
                item['Reviews'] = int(reviews)

            star_rate = response.xpath('//i[@data-hook="average-star-rating"]/span/text()').extract_first()
            if star_rate is None:
                item['Star_Rate'] = 'No star rate added'
            else:
                star_rate = star_rate.replace(" out of 5 stars", "")
                item['Star_Rate'] = float(star_rate)

            price = response.xpath('//ul[@id="mediaTabs_tabSet"]//li[@class="a-tab-heading a-active mediaTab_heading"]//div[@class="a-row"]/span/text()').extract()
            if price is None:
                item['Price'] = 'No price added'
            elif len(price) > 0:
                price = price[0] + ': ' + str(price[1]).strip()
                item['Price'] = str(price).strip()
            else:
                item['Price'] = 'No price added'

            img_url = response.xpath('//img[@id="imgBlkFront"]/@data-a-dynamic-image').extract_first()
            if img_url is None:
                item['Img_Url'] = 'No image added'
            else:
                img_url = img_url.split(':[')[0].strip('{"')
                item['Img_Url'] = str(img_url).strip()

                urlretrieve(img_url, pwd + "crawlImages/" + str(BookSpider.image_count))
                item['Img_Path'] = pwd + "crawlImages/" + str(BookSpider.image_count) + ".jpg"
                BookSpider.image_count = BookSpider.image_count + 1

        except Exception as error:
            logger.info(error)
        yield item
