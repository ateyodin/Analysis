
import tweepy
from textblob import TextBlob

consumer_key = 'your consumer key'
consumer_key_secret = 'your consumer key secrey'

access_token = 'your access token'
access_token_secret = 'your access token secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Batman')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")

