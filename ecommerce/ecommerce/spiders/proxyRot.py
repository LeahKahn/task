import requests
import scrapy

from .parseWeb import ComSpider

proxy = '52.183.8.192:3128'
try:
    r = requests.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1', \
                     proxies = {'http':proxy, 'https':proxy}, \
                     timeout = 3)
    works = ComSpider()
    print(works(r))
except:
    print("Failed")