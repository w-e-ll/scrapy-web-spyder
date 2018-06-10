# -*- coding: utf-8 -*-
import os
import sqlite3
con = None


class AmazonPipeline(object):

    def __init__(self):
        self.setup_db_con()
        self.create_tables()

    def setup_db_con(self):
        self.con = sqlite3.connect(os.getcwd() + '/test.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        self.drop_amazon_table()
        self.create_amazon_table()

    def drop_amazon_table(self):
        # drop amazon table if it exists
        self.cur.execute("DROP TABLE IF EXISTS Amazon_Book")

    def close_db(self):
        self.con.close()

    def __del__(self):
        self.close_db()

    def create_amazon_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Amazon_Book( \
                id INTEGER PRIMARY KEY UNIQUE NOT NULL, \
                title VARCHAR(500) NOT NULL, \
                description VARCHAR(200) NOT NULL, \
                paperback_price VARCHAR(20) NOT NULL, \
                author  VARCHAR(500) NOT NULL, \
                star_rate FLOAT NOT NULL, \
                reviews INTEGER NOT NULL, \
                img_url VARCHAR(500) NOT NULL, \
                img_path VARCHAR(500) NOT NULL\
                )")

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cur.execute("INSERT INTO Amazon_Book(\
                              title, \
                              description, \
                              paperback_price, \
                              author, \
                              star_rate, \
                              reviews, \
                              img_url, \
                              img_path) \
                              VALUES(?, ?, ?, ?, ?, ?, ?, ?)", \
                             ( \
                                 item.get('Title', ''),
                                 item.get('Description', ''),
                                 item.get('Paperback_Price', ''),
                                 item.get('Author', ''),
                                 item.get('Star_Rate', ''),
                                 item.get('Reviews', ''),
                                 item.get('Img_Url', ''),
                                 item.get('Img_Path', '')
                             ))
        print('------------------------')
        print('Data Stored in Database')
        print('------------------------')
        self.con.commit()
