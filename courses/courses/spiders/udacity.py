import scrapy


class UdacitySpider(scrapy.Spider):

    name = "udacity"
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
        print(divs)
        for div in divs:
            link = div.xpath('.//h3/a')
            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()
            img = div.xpath('.//img[contains(@class, "img-responsive")]/@src').extract_first()
            description = div.xpath('.//div[2]/div[2]/text()').extract_first()
            yield {
                'title': title,
                'url': href,
                'image': img,
                'description': description,
            }