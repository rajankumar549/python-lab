from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import  Stream
import time
import tweepy
import json

access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class StdoutListener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            sourcefile=open("real.txt","w+")
            sourcefile.write(data)
            sourcefile.write('\n')
            sourcefile.close()
        except Exception as e:
            print("try to resolve %s",str(e))
    def on_error(self, status):
        print(status)



""" l= StdoutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    stream=Stream(auth,l)"""
"""at=[]
at=api.user_timeline(screen_name="realdonaldtrupm",count=1)
i=len(at)-1"""
alltweets = []
new_tweets = api.user_timeline(screen_name="realdonaldtrump", count=200)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1

# keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    i=len(new_tweets)-1
    while i >= 0:
        status = new_tweets[i]
        json_str = json.dumps(status._json)
        sourcefile = open("tweets_realdonald.txt", "a+")
        sourcefile.write(json_str)
        sourcefile.write('\n')
        sourcefile.close()
        i = i - 1

    print("getting tweets before %s" % (oldest))
    new_tweets = api.user_timeline(screen_name="realdonaldtrump", count=200, max_id=oldest)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    print("...%s tweets downloaded so far" % (len(alltweets)))






