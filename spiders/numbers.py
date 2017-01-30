import scrapy


class numbersSpider(scrapy.Spider):
   name = "numbersver1"
   start_urls = ['http://www.the-numbers.com/movie/budgets/all']

   def parse(self, response):
    	for i in response.xpath('//tr'):
    		yield {

      		 'titel' : i.xpath('./td/b/a/text()').extract_first(),
      		 'release_date' : i.xpath('./td/a/text()').extract_first(),
      		 'rank' : i.xpath('./td[1]/text()').extract_first(),
      		 'production_budget' : i.xpath('./td[4]/text()').extract_first(),
      		 'domestic_gross' : i.xpath('./td[5]/text()').extract_first(),
      		 'worldwide_gross' : i.xpath('./td[6]/text()').extract_first(),
      		}

      		
      	
