# Amazon-Books-Crawler

Amazon-Books-Crawler is a python web crawler developed with Scrapy framework.
For now, it has only one spider, for crawling the search results from amazon.com. 
This crawler extracts the book title, description, paperback_price, author, star_rate, reviews, img_url, img_path and stores them in a sqlite3 database and JSON/CSV file. 
To read logs after crawling, read file named log.txt in main directory.

- Python3
- Scrapy
- SQLite3

## Installing Dependencies
1. virtualenv -p python3 scrapy_books_spyder
2. cd scrapy_books_spyder
3. activate it (source bin/activate)
4. git clone https://github.com/w-e-ll/scrapy-web-spyder.git
5. cd scrapy-web-spyder
6. cd app
7. pip install -r requirements.txt
8. cd /amazon
9. scrapy crawl amazon

made by: https://w-e-ll.com