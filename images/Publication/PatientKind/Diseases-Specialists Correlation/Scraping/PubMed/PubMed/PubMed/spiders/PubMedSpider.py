import scrapy

class PubMedSpider(scrapy.Spider):
    name = "PubMed"
    start_urls = [
        "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=Angelman+Syndrome&RetMax=1531"
    ]
    
    
    def parse(self, response):
        filename = response.url.split("/")[-2]+'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
