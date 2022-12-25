import requests
from bs4 import BeautifulSoup

import pandas

import parsing 


class Scraper:
    BASE_URL = 'https://www.basketball-reference.com'
    
    def __init__(self, parser):
        self.parser = parser

    def player_stats_per_game(self, year):
        url = f'{self.BASE_URL}/leagues/NBA_{year}_per_game.html'
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        stat_names = [stat_name.text for stat_name in soup.find('tr', {'class': 'thead'}).find_all('th')[1:]]
        rows = soup.find('tbody').find_all('tr', {'class': 'full_table'})
        
        stats_data = [{ stat_name: self.parser.stat_text_to_value(stat.text) for (stat_name, stat) in zip(stat_names, row.find_all('td')) }
         for row in rows]

        player_stats_df = pandas.DataFrame.from_dict(stats_data)
        
        # return player_stats_df
        
    
print('\n'*100)

s = Scraper(parser=parsing.Parser())
s.player_stats_per_game(year=2023)