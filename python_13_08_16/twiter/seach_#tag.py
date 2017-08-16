from __future__ import absolute_import, print_function
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv




def cs(tweet, name):
    path = str(name) + ".csv"
    try:
        file = open(path, "x", newline="")
    except Exception as e:
        e = FileExistsError

    # open a file for writing

    file = open(path, "r+", newline="")

    # create the csv writer object

    csvwriter = csv.writer(file)
    reader = csv.reader(file, delimiter=",")
    data = list(reader)
    row_count = len(data)

    data2 = ["Name",
             "Twitter Handle",
             "Total Tweet",
             "Total ReTweets",
             "Total Following",
             "Tolat Followers",
             "UserID",
             "User Verified",
             "User Location",

             "Date of Tweet",
             "Tweet ID",
             "Tweet Text",


             "Tweet ReTweet Status",

             "Tweet  Reply To ID"
             ]
    if (row_count < 1):
        csvwriter.writerow(data2)

    data2 = [
        tweet.user.name,
        tweet.user.screen_name,
        tweet.user.statuses_count,
        tweet.retweet_count,
        tweet.user.friends_count,
        tweet.user.followers_count,
        tweet.user.id_str,
        tweet.user.verified,
        tweet.user.location,
        tweet.created_at,
        tweet.id,
        tweet.text,
        tweet.retweeted,
        tweet.in_reply_to_user_id

    ]
    csvwriter.writerow(data2)
    file.close()
    print(tweet.user.name,
          tweet.user.screen_name,
          tweet.user.statuses_count,
          tweet.retweet_count,
          tweet.user.friends_count,
          tweet.user.followers_count,
          tweet.user.id_str,
          tweet.user.verified,
          tweet.user.location,
          tweet.created_at,
          tweet.id,
          tweet.text,
          tweet.retweeted,
          tweet.in_reply_to_user_id)




def search_has(name,limit):
    for tweet in tweepy.Cursor(api.search,
                               q=name,
                               rpp=100,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items(limit):
        try:
            cs(tweet,name)
        except:
            continue





if __name__ == "__main__":
    access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
    access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
    consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
    consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    search_has(name="#realdonaldtrump",limit=200)

