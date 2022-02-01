# This is a sample Python script.
import requests
import csv
import scrapy
from ecommerce.ecommerce.spiders.parseWeb import ComSpider


def extract(proxy):
    # count = 0
    try:
        r = requests.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
                         proxies={'http': proxy, 'https': proxy},
                         timeout=10)
        # count += 1
        # if count > 1:
        works = ComSpider()
        print(works.parse(r))
    except:
        print("Failed")


if __name__ == '__main__':
    proxylist = []
    with open('proxylist.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxylist.append(row[0])

    for i in proxylist:
        extract(i)
