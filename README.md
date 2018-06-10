# Amazon-Books-Crawler

Amazon-Books-Crawler is a python web spyder developed with Scrapy framework. 
For now, it has only one spider, it scrapes python books from  https://www.amazon.com search results. 
This spyder extracts book title, description, paperback_price, author, star_rate, reviews, img_url, img_path and stores results in a sqlite3 database. 
Also, data could be stored to a JSON or CSV file with a simple command -- scrapy crawl amazon - file.json. To read logs after crawling, read file named log.txt in main directory.

## Dependencies

- Python3
- Scrapy
- SQLite3

## Installing Dependencies
1. virtualenv -p python3 scrapy_books_spyder
2. cd scrapy_books_spyder
3. activate it (source bin/activate)
4. git clone https://github.com/w-e-ll/scrapy-web-spyder.git
5. cd scrapy-web-spyder
6. pip install -r requirements.txt
7. cd amazon
8. scrapy crawl amazon

made by: https://w-e-ll.com
