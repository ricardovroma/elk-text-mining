#! /usr/bin/sh

from sklearn.datasets import fetch_20newsgroups
import pandas as pd

from elasticsearch import Elasticsearch
import eland as ed

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "comp.sys.mac.hardware",
    "comp.windows.x",
    "misc.forsale",
    "rec.autos",
    "rec.motorcycles",
    "rec.sport.baseball",
    "rec.sport.hockey",
    "sci.crypt",
    "sci.electronics",
    "sci.med",
    "sci.space",
    "soc.religion.christian",
    "talk.politics.guns",
    "talk.politics.mideast",
    "talk.politics.misc",
    "talk.religion.misc",
]
newsgroups = fetch_20newsgroups(
  remove=("headers", "footers", "quotes"),
  subset="all",
  categories=categories
)

df = pd.DataFrame(data={
    'news': newsgroups.data,
    'category': newsgroups.target,
    'category_name': [categories[pos] for pos in newsgroups.target]
})

es = Elasticsearch('http://elasticsearch:9200')

ed.pandas_to_eland(
    pd_df=df,
    es_client=es,
    es_dest_index='20-newsgroups',
    es_if_exists='replace',
    es_type_overrides={'news': 'text', 'category_name': 'text'},
    es_refresh=True
)

es.close()