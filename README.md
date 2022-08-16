# NPL_Project

In this project I am exploring the aspects of natural language processing (NLP) and creation of own APIs.

For the sake of NLP a dataset of daily top 20 news headlines is analyzed. The dataset spans from 2008-08-08 to 2016-07-01 and contains 1989 days times 20 top headlines from Reddit World News Channel. In total aroud 40k of headlines.

The dataset is obtained from Kaggle:

https://www.kaggle.com/datasets/aaron7sun/stocknews

**Goals of the project**

The project has the followng goals:
- Read and clean the news headline dataset
- Analyze the frequency of words, classify the news and analyze their sentiment
- See if the news sentiment has any correlation with the market returns
- Upload the data to MySQL
- Create an API to call the data from and write to the the database

In order to vizualize the data I produce a word cloud. This is done by removing the "stop" words with Spacy package.

Below is the summary of the most common words in the news headlines:

<p align="center">
<img src="https://github.com/berserkus/NLP_Project/blob/main/images/word_cloud.png">
</p>

The frequency of words is shown in a bar chart:

<p align="center">
<img src="https://github.com/berserkus/NLP_Project/blob/main/images/word_count.png">
</p>


### Categorization of headlines

As some of the news refer to different categories, I first run an NLP model (RobertaForSequenceClassification) to classify the news. This model allows you to provide candidate categories, where the model checks the strings against these categories and provides a probability for them.

The model is unfortunately very slow, therefore I was only able to categorize only top 3 headline sources across the 8 years of data. The following categories were chosen [politics, economy, business, healthcare, entertainment, sports, weather].

For the remaining 17 columns, I have used the Machine learning algorithm Random Forest Classifier. The training of the model was done with the 1st column of headlines. However this model is very imprecise - since majority of the news are classified as politics

### Sentiment analysis

Next the sentiment of the news headlines are analyzed. It is done using the SentimentIntensityAnalyzer from NLTK.

For every news headline the sentiment of it is calculated. It returns between -1 and 1 where -1 is really negative and 1 is positive, anything between -0.05 and 0.05 is considered neutral.

It is interesting to see that the **overall sentiment of the news is rather negative**. This could be due to the reason that negative news catch more attention. The distribution of the sentiment is below:

<p align="center">
<img src="https://github.com/berserkus/NLP_Project/blob/main/images/sentiment_histogram.png">
</p>

While a single source of news is not very evenly distributed, the collection of them shows a shame much closer to the bell curve. However they are very much skewed to the negative side.


### Sentiment analysis as trading strategy?

In order to see if the news sentiment has any predictive power for a potential trading strategy we compare the daily news sentiment with the S&P 500 market returns.

I download the S&P 500 index returns from Yahoo Finance and merge it to the headline database.

**Correlation analysis**

<p align="center">
<img src="https://github.com/berserkus/NLP_Project/blob/main/images/correlation.png">
</p>
