import scrapy
from scrapy.selector import Selector
from dangdang.items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['https://search.dangdang.com/search?keyword=%E8%AE%A1%E7%AE%97%E6%9C%BA']

    def parse(self, response):
        item = DangdangItem()
        sel = Selector(response)
        item['title'] = sel.xpath('//div[@class="result"]/div[@class="book-info"]/h1/text()').extract()
        item['link'] = sel.xpath('//div[@class="result"]/div[@class="book-info"]/a/@href').extract()
        return item
