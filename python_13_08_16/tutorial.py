from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import  Stream
import time
import tweepy

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
            sourcefile=open("real.txt","a+")
            sourcefile.write(data)
            sourcefile.write('\n')
            sourcefile.close()
        except Exception as e:
            print("try to resolve %s",str(e))
    def on_error(self, status):
        print(status)


if __name__=='__main__':
    l= StdoutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    stream=Stream(auth,l)
   # stream = api.user_timeline('realdonaldtrump')

    stream.filter(track=['realdonaldtrump'])


