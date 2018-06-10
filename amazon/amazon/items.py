# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Book(Item):
    Title = Field()
    Description = Field()
    Author = Field()
    Star_Rate = Field()
    Price = Field()
    Reviews = Field()
    Img_Url = Field()
    Img_Path = Field()


class Product(Item):
    Title = Field()
    Sale_Price = Field()
    Category = Field()
    Original_Price = Field()
    Availability = Field()
