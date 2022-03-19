from crawler.googlenews_crawler import GoogleNews
import pandas as pd


def get_titles(search_key, time_interval, language, country):
    stories = []
    gn = GoogleNews(lang=language, country=country)
    search = gn.search(search_key, when=str(time_interval)+"d")
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'title': item.title
        }
        stories.append(story)
    return stories


def main_googlenews(key, timeinterval, language, country):
    df = pd.DataFrame(get_titles('intitle:' + key, timeinterval, language, country))
    lower_df = df['title'].str.lower()
    lower_df.to_csv('news_headlines.csv', index=False, header=True)
    print("Google News crawler finished")
