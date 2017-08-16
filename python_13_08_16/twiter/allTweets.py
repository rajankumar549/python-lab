from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import  Stream
import time
import tweepy
import json
import csv




def print_csv(new_tweets,handd):
        i = len(new_tweets) - 1
        while i >= 0:
                try:
                    cs(status=new_tweets[i],name=handd)
                except :
                        print("Exception",len(new_tweets) - 1,i)
                        i = i - 1


                i = i - 1

def get_tweets(handller,limit):
        alltweets = []
        new_tweets = api.user_timeline(screen_name=handller, count=200)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while (len(new_tweets) > 0 and len(alltweets)<=limit):
                print_csv(new_tweets=new_tweets,handd=handller)
                print("getting tweets before %s" % (oldest))

                new_tweets = api.user_timeline(screen_name=handller, count=200, max_id=oldest)
                alltweets.extend(new_tweets)
                oldest = alltweets[-1].id - 1
                print("...%s tweets downloaded so far" % (len(alltweets)))

def cs(status,name):
        path=str(name)+".csv"
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
                 "Total Following",
                 "Tolat Followers",
                 "UserID",
                 "User Verified",
                 "User Location",
                 "User Description",
                 "Date of Tweet",
                 "Tweet ID",
                 "Tweet Text",
                 "Tweet_Lang",
                 "Tweet Source",
                 "Tweet ReTweet Status",
                 "Tweet  Reply To Name",
                 "Tweet  Reply To ID"
                 ]
        if (row_count < 1):
                csvwriter.writerow(data2)

        data2 = [
                 status.user.name,
                 status.user.screen_name,
                 status.user.statuses_count,
                 status.user.friends_count,
                 status.user.followers_count,
                 status.user.id_str,
                 status.user.verified,
                 status.user.location,
                 status.user.description,
                 status.created_at,
                 status.id,
                 status.text,
                 status.lang,
                 status.source,
                 status.retweeted,
                 status.in_reply_to_screen_name,
                 status.in_reply_to_user_id

                 ]
        csvwriter.writerow(data2)
        file.close()
        print(status.user.name,
              status.user.screen_name,
              status.user.statuses_count,
              status.user.friends_count,
              status.user.followers_count,
              status.user.id_str,
              status.user.verified,
              status.user.location,
              status.user.description,
              status.created_at,
              status.id,
              status.text,
              status.lang,
              status.source,
              status.retweeted,
              status.in_reply_to_screen_name,
              status.in_reply_to_user_id)


if __name__=="__main__":
        access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
        access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
        consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
        consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        get_tweets("realdonaldtrump",200)












