from googlenews_crawler import GoogleNews
import pandas as pd


def get_titles(search_key, time_interval):
    stories = []
    gn = GoogleNews(lang='EN',country='UK')
    search = gn.search(search_key, when=str(time_interval)+"d")
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'title': item.title
        }
        stories.append(story)
    return stories


def main_googlenews(key):
    df = pd.DataFrame(get_titles('intitle:' + key, 10))
    df.to_csv('news_headlines.csv', index=False, header=False)


if __name__ == "__main__":
    main_googlenews('Burger King')