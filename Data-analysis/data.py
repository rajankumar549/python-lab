import tweepy
from tweepy import OAuthHandler





if __name__ == "__main__":
    access_key = "802832002592317440-ihDftIUNWmfgm8qMQ3MB31Kpqla5bhA"
    access_secret = "v71yIkPWddq2ILlqNxp75gMXgqZpNfHYcwDnnzI9RuOnc"
    consumer_key = "XhIt0CHA1GszgF6zs1Y1NmZps"
    consumer_secret = "3GdpDAfOUf5oaedyx3JsCIVxxYa0pYl1pNHG2qqcIGLe6vSGnI"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    arr=[]
    k=api.user_timeline(id="sabtv",count=2)
    i=0
    while(1):
        arr.extend(k)
        for y in k:
            print("arr["+str(i)+"]="+str(y.id)+y)
            i+=1
        print("end[x]="+str(arr[-1].id))
        k = api.user_timeline(id="sabtv", count=2,max_id=arr[-1].id-1)
   # for status in k:
        # Process a single status
   #     print(status.user.screen_name + "\n" + status.text)
     #   print("-------------------------")
   # v= api.me()
    #for status in tweepy.Cursor(api.home_timeline).items(10):
     #   #Process a single status
     #    print(status.user.screen_name+"\n"+status.text)
     #   print("-------------------------")
    #print(v.screen_name)



