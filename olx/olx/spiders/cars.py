import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']
    start_urls = ['http://pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li')
        for item in items: 
            self.log(item.xpath('./a/@href').extract_first())
