import pymysql
import datetime as dt
db = pymysql.connect(host='35.167.255.90',port=3306,user='root',passwd='Needsforblood@12321')
cursor = db.cursor()
cursor.execute("SHOW DATABASE")
for row in cursor:
    print(row)
"""import csv
fs=open('pincodes_tab.csv', 'r+')
reader = csv.reader(fs)
for row in reader:
    try:
        cursor.execute("insert into pin_dir values ('"+str(row[0])+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5]) +"','"+str(row[6])+ "','" + str(row[7])+ "','" + str(row[8])+ "','" + str(row[9])+"');\n");
    except Exception as e:
        continue

db.commit()"""