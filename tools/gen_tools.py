import pandas as pd
from newsapi import NewsApiClient
import dotenv
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia=SentimentIntensityAnalyzer()

dotenv.load_dotenv()
pass_w=os.getenv("news_api_key")

newsapi = NewsApiClient(api_key=pass_w)

def cur_news(source,date):
    all_articles = newsapi.get_everything(sources=source,
                                      from_param=date,
                                      to=date,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    
    news_string=[]
    for i in all_articles['articles']:
        news_string.append(i['publishedAt']+' '+i['title']+ ' - sentiment: '+str(sia.polarity_scores(i['title'])['compound'])+'<br>')
    
    return str(news_string)