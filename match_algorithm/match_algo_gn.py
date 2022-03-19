# Use "core-competitiveness" as an example

import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv('news_headlines.csv')
processed_list_pos_CC = []
processed_list_neg_CC = []


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def similar_test(to_test):
    for item in processed_list_pos_CC:
        if similar(to_test, item) > 0.9:
            return False
    return True


pos_list_CC = {
    'world-first': 1,
    'popular': 0.5,
    'tasty': 0.4,
    'award': 0.6
}
neg_list_CC = {
    'shit': 1,
    'cheap': 0.2,
    'positive covid': 0.3,
    'halt': 0.7
}

pos_score_CC = 0.0
neg_score_CC = 0.0


def main_algo():
    global pos_score_CC
    global neg_score_CC
    for index, row in df.iterrows():
        for word in pos_list_CC.keys():
            if word in row["title"]:
                if similar_test(word):
                    pos_score_CC = pos_score_CC + pos_list_CC[word]
                    print("pos_score_changed: " + str(pos_score_CC) + " " + word + " / " + row["title"])
                    processed_list_pos_CC.append(word)
        for word in neg_list_CC.keys():
            if word in row["title"]:
                if similar_test(word):
                    neg_score_CC = neg_score_CC + neg_list_CC[word]
                    print("neg_score_changed: " + str(neg_score_CC) + " " + word + " / " + row["title"])
                    processed_list_neg_CC.append(word)

    print("final positive score: " + str(pos_score_CC))
    print("final negative score: " + str(neg_score_CC))
