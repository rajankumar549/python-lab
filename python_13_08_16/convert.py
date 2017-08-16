import json
teweet_path="tweets_realdonald.txt"
t_file=open(teweet_path,"r+")
print(t_file)
tweet=[]
i=0
json_file = open("alltweets_realdonald.json","a+")
with open("real.txt","r") as f:
     for line in f:
           try:

             tweet.append(json.loads(line))
             i=i+1
             print(line)
             print("\n")
           except Exception as e:
            print(str(e))
print(i)
json.dump(tweet,json_file,indent=4)
