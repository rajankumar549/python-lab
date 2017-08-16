import pymongo
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.DataAnalysis
grades = db.upelection_data2
cursor = grades.find()
i=0
y=0
hi=0
other=0
en=0
for x in cursor:
    i+=1
    #x=json.load(x)
    print("precessing tweet no"+str(i))
    if(x["lang"]=="hi"):
        hi+=1
    elif(x["lang"]=="en"):
        en+=1
    else:
        other+=1
raw_data = {'language': ['Hindi', 'English', 'Other'],
             'value': [hi,en,other],}
df = pd.DataFrame(raw_data, columns=['language', 'value'])
print(df)
# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59"]
plt.pie(
    # using data total)arrests
    df['value'],
    # with the labels being officer names
    labels=df['language'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    #explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()



