import json
import pandas as  pd
import matplotlib.pyplot as plt


tweets_data_path ="data.txt"
tweets_data=[]
fp=open(tweets_data_path,"r")

for line in fp:
    try:

        tweet=json.loads(line)


        tweets_data.append(tweet)
    except:
        continue
print( tweet['text'])

#tweets=pd.DataFrame()
#tweets["text"]=map(lambda tweet:tweet['text'],tweets_data)
#tweets["lang"]=map(lambda tweet:tweet['lang'],tweets_data)
#tweets["country"]=map(lambda tweet:tweet['place']['country']if['place']!=None else None,tweets_data)

#tweets_by_lang=tweets['lang'].value_counts()
#print(tweets['lang'].value_counts())

#print(tweets['lang'].va)
#fig,ax=plt.subplots()
#ax.tick_params(axis='x',labelsize=15)
#ax.tick_params(axis='y',labelsize=10)
#ax.set_xlabel(tweets["lang"],fontsize=15)
#ax.set_ylabel('no of tweet',fontsize=15)
#ax.set_title('top 5 languages',fontsize=15,fontweight='bold')
#tweets_by_lang[:5].plot(ax=ax,kind='bar',color='white')
#plt.show()


