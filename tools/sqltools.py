from config.sqlconfig import engine
import pandas as pd
import json

def get_news(date):
    query=f"""SELECT Top1, Top2, Top3, 
    sentiment_Top1, sentiment_Top2, sentiment_Top3,
    total_sentiment, Returns
    FROM news
    WHERE Date='{date}'"""

    news=pd.read_sql_query(query, engine).to_json(orient='records')

    return news