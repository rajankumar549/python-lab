import csv
with open('pincodes_tab.csv', 'r+') as f:
    reader = csv.reader(f)
    fo = open("foo.sql", "w+")
    i=0
    for row in reader:
        i += 1
        if(i==1):
            continue

        temp= "insert into pin_dir values ('"+str(row[0])+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5]) +"','"+str(row[6])+ "','" + str(row[7])+ "','" + str(row[8])+ "','" + str(row[9])+"');\n"
        print(temp)
        fo.write(temp)

