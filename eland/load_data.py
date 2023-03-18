#! /usr/bin/sh

from sklearn.datasets import fetch_20newsgroups
import pandas as pd

from elasticsearch import Elasticsearch
import eland as ed

df = pd.read_csv('./Corona_NLP_test.csv', usecols=['ScreenName', 'OriginalTweet', 'Sentiment', 'TweetAt'])
es = Elasticsearch('http://127.0.0.1:9200')

ed.pandas_to_eland(
    pd_df=df,
    es_client=es,
    es_dest_index='corona',
    es_if_exists='replace',
    es_type_overrides={
        'ScreenName': 'text',
        'OriginalTweet': 'text',
        'Sentiment': 'text',
        'TweetAt': 'text',
    },
    es_refresh=True
)

es.close()