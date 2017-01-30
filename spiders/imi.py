import pandas as pd
df = pd.read_csv('/Users/srs/Dropbox/GitHub/ProjectLuther/imdb/imdbDirector1.csv')
imdblist = df['link']

import scrapy

class imdb(scrapy.Spider):
    name = "imi1"
    start_urls = ['http://www.imdb.com/title/tt0110912']

    def parse(self, response):
        

        for i in response.xpath('//div[@id="tn15content"]/h5[1]/text()').extract():
            

            yield {i : response.xpath('//div[@class="business"]/div[3]/div[3]/text()[2]').extract()
            }

        for i in imdblist:
            next_page = 'http://www.imdb.com'+i+'business?ref_=tt_dt_bus'
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
