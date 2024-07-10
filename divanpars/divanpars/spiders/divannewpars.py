import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ['https://www.divan.ru/category/stoly-i-stulya']

    def parse(self, response):
        stolys = response.css('div.WdR1o')
        for stoly in stolys:
           if stoly:
            yield {
                'name' : stoly.css('div.wYUX span::text').get(),
                'price' : stoly.css('div.HMCQY span::text').get(),
                'url' : stoly.css('a').attrib['href']
            }
