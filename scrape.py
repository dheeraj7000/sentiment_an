"""snsScrape is a web scraper tool designed to extract data from social media platforms. 
It allows users to gather large amounts of data from various social networks such as 
Twitter, Facebook, and Instagram. snsScrape is capable of extracting various types of 
data including posts, comments, likes, shares, and other information. 
The tool is built using Python and utilizes various libraries and APIs to extract the data.
The scraped data can be saved in various formats such as CSV, JSON, or SQL for further analysis and processing. 
snsScrape is a valuable tool for researchers, marketers, and data scientists who are looking to gather 
insights from social media platforms. With snsScrape, users can easily collect and analyze large amounts of 
social media data, which can be used to gain a better understanding of consumer behavior, trends, and opinions."""

import snscrape.modules.twitter as sntwitter 
import pandas as pd
import json

query = " (chatgpt) (ai) (#chatgpt OR #ai) lang:en until:2023-01-01 since:2020-01-01 -filter:links -filter:replies"
tweets = []
limits =  50000
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # print(vars(tweet))
        # break
        if len(tweets) == limits:
            break
        else:
            tweets.append([tweet.date, tweet.content])
df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
df.to_csv(r'C:\Users\Asus\Desktop\AI research\scraped.csv')
