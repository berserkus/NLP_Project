import pandas as pd
import re
import spacy
from collections import Counter
import operator
import stylecloud
from IPython.display import Image
import pandas_datareader as pdr

# function to clean the dataframe
def clean_data(df):
    df.replace('b"', '', regex=True,inplace=True)
    df.replace("b'", "", regex=True,inplace=True)
    df.replace("'", "", regex=True,inplace=True)
    df.replace('"', "", regex=True,inplace=True)

    df['Combined']=df['Top1']+' '+df['Top2']+' '+df['Top3']+' '+df['Top4']+' '+df['Top5']\
    +' '+df['Top6']+' '+df['Top7']+' '+df['Top8']+' '+df['Top9']+' '+df['Top10']\
    +' '+df['Top11']+' '+df['Top12']+' '+df['Top13']+' '+df['Top14']+' '+df['Top15']\
    +' '+df['Top16']+' '+df['Top17']+' '+df['Top18']+' '+df['Top19']+' '+df['Top20']\


    return df


def long_string(df):

    # put all the news into one string
    long_string=''
    for index, row in df.iterrows():
        long_string+=' '+str(row['Combined'])

    # from the long string remove the stop words
    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words

    word_list_nstop = []
    # replace any expression of US to USA
    long_string=long_string.replace('U.S.A.','USA')
    long_string=long_string.replace('U.S.','USA')
    long_string=long_string.replace('US ','USA ')
    long_string=long_string.replace('US.','USA.')
    long_string=long_string.replace('US,','USA,')
    long_string=long_string.replace('United States of America','USA')
    long_string=long_string.replace('United States','USA')
    long_string = re.sub("\.|!|\?|,", '', long_string)
    long_string=long_string.lower()
    long_string_split=re.split("\s",long_string)
    # remove stop names
    for element in long_string_split:
        if element not in stop:
            word_list_nstop.append(element)
            
    # count the most frequent words
    words_dict=Counter(word_list_nstop)
    words_dict=sorted(words_dict.items(), key=operator.itemgetter(1),reverse=True)

    with open('long_string.txt', 'w') as f:
        f.write(long_string)

    stylecloud.gen_stylecloud(file_path='./long_string.txt',
                            icon_name='fas fa-cloud',
                            palette='cartocolors.diverging.TealRose_7',
                            background_color='white',
                            gradient='horizontal')

    df_words=pd.DataFrame(words_dict)
    df_words.columns=['word','count']
    df_words.drop([0,1],axis=0,inplace=True)
    
    return df_words

def yfinance_get(ticker,start_date,end_date):

    data = pdr.yahoo.daily.YahooDailyReader(symbols=ticker, start=start_date, end=end_date)
    df_sp = data.read()
    df_sp=df_sp.iloc[:, df_sp.columns.get_level_values(0)=='Adj Close']
    returns=df_sp[['Adj Close']].pct_change(1)
    returns=returns.rename(columns={'Adj Close': 'Returns'},level=0)
    df_sp=pd.concat([df_sp, returns], axis=1)
    df_sp.index.name=None
    df_sp.columns = df_sp.columns.to_flat_index()
    df_sp.columns=['S&P 500','Returns']
    df_sp['Date']=df_sp.index
    df_sp=df_sp[['Date','S&P 500','Returns']]
    df_sp['Date']=df_sp['Date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    
    return df_sp


