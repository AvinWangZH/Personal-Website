import scrapy

class GeneReviewSpider(scrapy.Spider):
    name = "geneReview"
    start_urls = [
        "http://www.ncbi.nlm.nih.gov/books/NBK1116/"
    ]

#This is the right path to get the data: response.xpath('//ul[@id="toc_tllNBK1116_del1p36"]/li[@class]/*').extract()
def parse(self, response):
    for sel in response.xpath('//ul[@id="toc_tllNBK1116_del1p36"]/li[@class]/*'):
        item = GenereviewItem
        item['title'] = sel.xpath('a/text()').extract()
        item['author_names'] = sel.xpath('a/@href').extract()
        yield item
        