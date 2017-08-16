from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pymongo
from pymongo import MongoClient
import sys
import time
import tweepy
import json

access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"
connection = MongoClient('localhost',27017)
db = connection.DataAnalysis
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
db = connection.DataAnalysis
def convert( self ,status ):
    data2 = {
        "name": str(status.user.name),
        "screen_name": str(status.user.screen_name),
        "statuses_count": str(status.user.statuses_count),
        "friends_count": str(status.user.friends_count),
        "followers_count": str(status.user.followers_count),
        "id_str": str(status.user.id_str),
        "verified": str(status.user.verified),
        "location": str(status.user.location),
        "description": str(status.user.description),
        "created_at": str(status.created_at),
        "_id": str(status.id),
        "text": str(status.text),
        "lang": str(status.lang),
        "source": str(status.source),
        "retweeted": str(status.retweeted),
        "in_reply_to_screen_name": str(status.in_reply_to_screen_name),
        "in_reply_to_user_id": str(status.in_reply_to_user_id)

    }
    return data2

class StdoutListener(StreamListener):
    #def on_data(self, data):
     #   try:
    #        print("data---")
      #      data=json.loads(data)
     #       #db.upelection.insert(convert(data))
     #       print(data.text)
     #       exit()



      #  except Exception as e:
      #      print(e)
      #      exit()
    def on_status(self, status):



            data2 = {
                "name": str(status.user.name),
                "screen_name": str(status.user.screen_name),
                "statuses_count": str(status.user.statuses_count),
                "friends_count": str(status.user.friends_count),
                "followers_count": str(status.user.followers_count),
                "id_str": str(status.user.id_str),
                "verified": str(status.user.verified),
                "location": str(status.user.location),
                "description": str(status.user.description),
                "created_at": str(status.created_at),
                "_id": str(status.id),
                "text": str(status.text),
                "lang": str(status.lang),
                "source": str(status.source),
                "retweeted": str(status.retweeted),
                "in_reply_to_screen_name": str(status.in_reply_to_screen_name),
                "in_reply_to_user_id": str(status.in_reply_to_user_id)

            }
            print(data2)
            db.upelection_data2.insert(data2)
            print(status.text)


    def on_error(self,status):
        print(status)


if __name__=='__main__':
    l= StdoutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    stream=Stream(auth,l)
   # stream = api.user_timeline('realdonaldtrump')

    stream.filter(track=["#upelection","#up"])
