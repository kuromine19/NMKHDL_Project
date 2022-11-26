import scrapy
import json
import re
import pandas as pd
import numpy as np

class collect_player_info(scrapy.Spider):
    name='films_info'
  
    def __init__(self):
        try:
            with open('dataset/films_urls.json') as f:
                self.players = json.load(f)
#             self.player_count = 1
        except IOError:
             print("File not found")

    def start_requests(self):
        urls = ['https://www.imdb.com/title/tt0068646/?ref_=ttls_li_tt']
        response = scrapy.Request(url = urls[0], callback=self.parse)
        yield response
        
    def parse(self, response):
        # IMDb rating
        IMDb_rating = response.css("span.sc-7ab21ed2-1::text").get()
        # Popularity
        popularity = response.css("div.sc-edc76a2-1::text").get()
        # User reviews
        user_reviews = response.css("span.three-Elements:contains(User\ reviews) span::text").get()
        # Critic reviews
        critic_reviews = response.css("span.three-Elements:contains(Critic\ reviews) span::text").get()
        # Metascore
        meta_score = response.css("span.score-meta::text").get()
        # Oscar wins
        oscar_wins = response.css("a[href*=awards]::text").get().split(" ")[1]
        

           
        yield({"IMDb RATING": IMDb_rating,
               "Popularity" : popularity,
               "User reviews": user_reviews,
               "Critic reviews": critic_reviews,
               "Meta score": meta_score,
               "Oscar wins": oscar_wins,
              })
#         if self.player_count < len(self.players):
#             next_page_url = 'https://sofifa.com/player/' + self.players[self.player_count]['player_url'] + '?units=mks'
#             self.player_count += 1
#             yield scrapy.Request(url=next_page_url, callback=self.parse) 