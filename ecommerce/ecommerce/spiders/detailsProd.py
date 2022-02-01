import scrapy

class parsedItems(scrapy.Item):
    price = scrapy.Field()
    title = scrapy.Field()
    stock = scrapy.Field()
    maftr = scrapy.Field()
