from crawler import main_gn as gn, main_twi as twi

# Crawl "KFC" on GoogleNews.UK for recent 10 days in English
gn.main_googlenews('KFC', 10, 'EN', 'UK')

# Crawl "KFC in UK" on Twitter
twi.main_twitter('KFC in UK')
