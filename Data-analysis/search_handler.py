import tweepy
from requests import HTTPError
from tweepy import OAuthHandler
import pymongo
from pymongo import MongoClient

import sys
import json





if __name__ == "__main__":
    connection = MongoClient('localhost', 27017)
    db = connection.DataAnalysis
    access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
    access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
    consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
    consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    i=0
    k=0
    user_count=0
    try:
        handller_result= api.search_users(q="#bjp",page=k)
        while(user_count<=200):
            for user in handller_result:
                # Process a single status
                #print(str(i)+"  "+str(user.screen_name)+"  "+ str(user.verified))
                if(user.verified):
                    user_data={ "_id":user.id,
                                 "name":user.name,
                                 "screen_name":user.screen_name,
                                 "id_str":user.id_str,
                                 "friends_count":user.friends_count,
                                 "verified":user.verified,
                                 "description":user.description,
                                 "created_at":user.created_at,
                                 "favourites_count":user.favourites_count,
                                 "followers_count":user.followers_count,
                                 "location":user.location,
                                 "statuses_count":user.statuses_count
                                 }
                    try:
                         print("user handller inserted"+str(user.screen_name))
                         print("----------------------------------------")
                         db.bjp_handller.insert(user_data)
                         user_count +=1
                    except Exception as ex:
                         print("skip")

                i+=1

            k+=1
            handller_result = api.search_users(q="#Congress", page=k)
    except HTTPError as ex:
        print(ex.response.status_code)
    # v= api.me()
    #for status in tweepy.Cursor(api.home_timeline).items(10):
    #   #Process a single status
    #    print(status.user.screen_name+"\n"+status.text)
    #   print("-------------------------")
    #print(v.screen_name)



