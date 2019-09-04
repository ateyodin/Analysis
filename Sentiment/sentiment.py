
import tweepy
from textblob import TextBlob

consumer_key = 'zGpPKUIsK9OiDts52xPjM115w'
consumer_key_secret = 'SRWlPssk83FjLC8Gzte2Jm6QhwxkswCAtr0sFi0gD0F5MTfpyA'

access_token = '195479346-gRyGSgxKl4PgGtGeTLYuZdQV2zpscvSOMdUYdmZU'
access_token_secret = 'VI10pMpk3BDY4S1TvZHBfoBJBiui4uBTdtaW4hJQS0Dbu'


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

    #elif analysis.sentiment[0]<0:
		#print ('Negative')
    #else:
        #print ('Neutral')
