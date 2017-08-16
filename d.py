#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"
access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    print('hiiiiiii')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        print(new_tweets)
        sourcefile = open("tweets_realdonald.txt", "a+")
        sourcefile.write(str(new_tweets["0"]))
        sourcefile.write('\n')
        sourcefile.close()
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))



    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("realdonaldtrump")
