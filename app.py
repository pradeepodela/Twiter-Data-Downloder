import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st


st.title("Twitter data downloader")
#query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
query = st.text_input("Query", "from:elonmusk until:2022-01-01 since:2010-01-01")
limit = st.number_input("Limit", value=100, min_value=1)
tweets = []
if st.button("Download"):
    st.write("Downloading tweets...")



    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        
        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            link = f'https://twitter.com/{tweet.username}/status/{tweet.id}'
            tweets.append([tweet.date, tweet.username, tweet.content,tweet.id,link])
            
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet','Id','Link'],index=None)


    # to save to csv
    st.write(df)
    df.to_csv('tweets.csv')