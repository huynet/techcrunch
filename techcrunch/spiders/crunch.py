import scrapy

class CrunchSpider(scrapy.Spider):
    name = "crunch"
    allowed_domains = ["www.techcrunch.com"]
    start_urls = [
        'http://www.techcrunch.com/page/1/',
        'http://www.techcrunch.com/page/2/',
        'http://www.techcrunch.com/page/3/',
        'http://www.techcrunch.com/page/4/',
        'http://www.techcrunch.com/page/5/',
    ]

    def parse(self, response):

        links = response.css('figure.post-block__media a').xpath('@href').extract()
        titles = response.css('a.post-block__title__link::text').extract()
        dates = response.css('time.river-byline__time::text').extract()
        datetimes = response.css('time.river-byline__time').xpath('@datetime').extract()
        authors = response.css('span.river-byline__authors a::text').extract()
        author_links = response.css('span.river-byline__authors a').xpath('@href').extract()
        captions = response.css('div.post-block__content::text').extract()
        images = response.css('figure.post-block__media a img').xpath('@src').extract()

        for i in range(20):
            yield {
                'link': links[i],
                'title': titles[i].strip(),
                'date': dates[i].strip(),
                'datetime': datetimes[i],
                'author': authors[i].strip(),
                'author_link': author_links[i],
                'caption': captions[i].strip(),
                'image': images[i]
            }
