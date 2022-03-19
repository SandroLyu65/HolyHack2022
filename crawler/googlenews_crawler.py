import feedparser
from bs4 import BeautifulSoup
import requests


class GoogleNews:
    def __init__(self, lang='en', country='US'):
        self.lang = lang.lower()
        self.country = country.upper()
        self.BASE_URL = 'https://news.google.com/rss'

    def parser_top_news(self, text):
        try:
            bs4_html = BeautifulSoup(text, "html.parser")
            lis = bs4_html.find_all('li')
            sub_articles = []
            for li in lis:
                try:
                    sub_articles.append({"url": li.a['href'],
                                         "title": li.a.text,
                                         "publisher": li.font.text})
                except:
                    pass
            return sub_articles
        except:
            return text

    def set_lan_cou_ceid(self):
        # https://news.google.com/search?q=burger%20king&hl=en-GB&gl=GB&ceid=GB%3Aen
        return '&ceid={}:{}&hl={}&gl={}'.format(self.country, self.lang, self.lang, self.country)

    def sub_articles(self, entries):
        for i, val in enumerate(entries):
            if 'summary' in entries[i].keys():
                entries[i]['sub_articles'] = self.parser_top_news(entries[i]['summary'])
            else:
                entries[i]['sub_articles'] = None
        return entries

    def parse_feed(self, feed_url):
        r = requests.get(feed_url)
        if 'https://news.google.com/rss/unsupported' in r.url:
            raise Exception('This feed is not available')
        d = feedparser.parse(r.text)
        if len(d['entries']) == 0:
            d = feedparser.parse(feed_url)
        return dict((k, d[k]) for k in ('feed', 'entries'))

    def search(self, query: str, when=None, from_time=None, to_time=None):
        if when:
            query += ' when:' + when
        search_ceid = self.set_lan_cou_ceid()
        # https://news.google.com/search?q=burger%20king&hl=en-GB&gl=GB&ceid=GB%3Aen
        d = self.parse_feed(self.BASE_URL + '/search?q={}'.format(query) + search_ceid)
        d['entries'] = self.sub_articles(d['entries'])
        return d