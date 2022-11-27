import scrapy
import json

class collect_player_info(scrapy.Spider):
    name='players_info'
    def __init__(self):
        try:
            with open('/KHDL/Lab_CK/film_crawler/film_crawler/dataset/films_urls.json') as f:
                self.players = json.load(f)
            self.player_count = 1

        except IOError:
            print("File not found")


    def start_requests(self):
        urls = ['https://www.imdb.com/title/tt0068646/?ref_=ttls_li_i']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        Director = response.xpath('//div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').extract()
        Writers = response.xpath('//div[3]/div[2]/div[1]/div[3]/ul/li[2]/div/ul/li/a/text()').extract()
        Stars = response.xpath('//div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()').extract()
        User_reviews = response.xpath('//div[3]/div[2]/div[2]/ul/li[1]/a/span/span[1]/text()').get()
        Critic_reviews = response.xpath('//div[3]/div[2]/div[2]/ul/li[2]/a/span/span[1]/text()').get()
        Metascore = response.xpath('//div[3]/div[2]/div[2]/ul/li[3]/a/span/span[1]/span/text()').get()
        yield {
            'Director':Director,
            'Writers':Writers,
            'Stars':Stars,
            'User_reviews':User_reviews,
            'Critic_reviews':Critic_reviews,
            'Metascore':Metascore,
        }
        if self.player_count < len(self.players):
            next_page_url = 'https://www.imdb.com/title/' + self.players[self.player_count]['ID'] + '/?ref_=ttls_li_i'
            self.player_count += 1
            yield scrapy.Request(url=next_page_url, callback=self.parse) 