import json
f=open("tweet.json","r")
tweet=[]
i=0
tweet=json.load(f)

for line in tweet:

     print(line["id"]["timestamp_ms"])
     i=i+1
     print("\n")

