from crawler import main_gn as gn, main_twi as twi
from match_algorithm import match_algo_gn as algo

gn.main_googlenews('KFC', 'EN', 'UK')  # If you change the language and country, please run twice to get actual data
twi.main_twitter('KFC in UK')

algo.main_algo()