from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request

class CrawlingSpider(CrawlSpider):
    name = "myfancycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    # Define rules for following links
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")), Rule(LinkExtractor(allow="catalogue",deny = "category",callback ="parse_item")),
    )
    def parse_item(self, response):
        