import pandas as pd
import quandl as q
df=q.get("NSE/BHARTIARTL", authtoken="rRGr7yB-Tqasubm6hAss")
df['Div']=df['High']-df['Low'];
df['Per_change']=(df['Close']-df['Open'])/df['Open']*100
df=df[['Open','Close','Div','Per_change']]
for_col='Close'
df.fillna(-99999,inplace=True)
for_out=(int)(len(df)*.00001)
df['nextday']=df[for_col].shift(-for_out)
print(df.head())
##for i in df.head():
# print(i)