import snscrape.modules.twitter as twitter
import streamlit as st
import pandas as pd
from pymongo import MongoClient
from bson import json_util

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017')
db = client["twitter_data"]

st.set_page_config(page_title="Twitter Scraper", page_icon=":guardsman:", layout="wide")

st.title("Twitter Scraper")

# Get search keyword or hashtag
keyword = st.text_input("Enter keyword or hashtag to search",value='enter keyword')

# Get date range
start_date = st.date_input("Enter start date (YYYY-MM-DD)")
end_date = st.date_input("Enter end date (YYYY-MM-DD)")

# Get tweet count limit
tweet_count = st.number_input("Enter tweet count limit", value=100)

# scrape the data and convert into dataframe and json
tweet1 = []
for i,tweet in enumerate(twitter.TwitterSearchScraper(f'{keyword} since:{start_date} until:{end_date}').get_items()):
    if i > tweet_count:
        break
    tweet1.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user,tweet.replyCount, tweet.retweetCount,tweet.lang, tweet.source, tweet.likeCount])    
tweets_df = pd.DataFrame(data=tweet1, columns=["Datetime", "ID", "URL", "Text", "User", "Reply Count", "Retweet Count", "Language", "Source", "Like Count"])
data = json_util.loads(tweets_df.to_json(orient='records'))
# display the scraped data

if st.button("Scrape Tweets"):
    st.dataframe(tweets_df)

# Store tweets in MongoDB
if st.button("Store in MongoDB"):
    # Create a collection for the current keyword
    collection_name = keyword 
    collection = db[collection_name]
    
    # Insert the json file to collection
    collection.insert_many(data) 
    st.write("Stored in MongoDB!")

# Download tweets as CSV
if st.button("Download as CSV"):
    st.write("Downloading...")
    tweets_df.to_csv("tweets.csv", index=False)
    st.write("Downloaded!")

# Download tweets as JSON
if st.button("Download as JSON"):
    st.write("Downloading...")
    tweets_df.to_json('tweets.json')
    st.write("Downloaded!")
