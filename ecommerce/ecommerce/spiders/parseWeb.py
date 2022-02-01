import sys
import scrapy
from .detailsProd import parsedItems


class ComSpider(scrapy.Spider):
    name = 'comm'
    start_urls = [
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
    ]

    def parse(self, response):
        items = parsedItems()
        all_items = response.css('div.product')
        for data in all_items:
            title = data.xpath(".//a[@class='catalog-item-name']/text()").extract()
            price = data.xpath(".//span[@class='']/text()").extract()
            if data.xpath(".//span[@class='out-of-stock']/text()")[0].extract() == 'Out of Stock':
                stock = False
            else:
                stock = True
            maftr = data.xpath(".//a[@class='catalog-item-brand']/text()").extract()

            items['price'] = price
            items['title'] = title
            items['stock'] = stock
            items['maftr'] = maftr

            yield items