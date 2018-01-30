# code returns max_tweets number of tweets (id + screen name of the creator + text) on the query

import tweepy
import csv

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
query = 'Referendum'
max_tweets = 20
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
for tw in searched_tweets:
    print(tw.id, ' ', tw.user.screen_name, ' ', tw.text)