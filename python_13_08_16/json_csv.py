
employee_data ='{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'

import json

import csv

employee_parsed = json.loads(employee_data)

emp_data = employee_parsed['employee_details']
try:
    employ_data = open('EmployData.csv', "x", newline="")
except Exception as e:
    e=FileExistsError





# open a file for writing

employ_data = open('EmployData.csv', "r+",newline="")

# create the csv writer object

csvwriter = csv.writer(employ_data)
reader = csv.reader(employ_data, delimiter=",")
data = list(reader)
row_count = len(data)

print(row_count)
data2=["first","last"]
if(row_count<1):
    csvwriter.writerow(data2)
var="rajan"
data2=[var,"kumar"]
i=0
while(i<10):
     csvwriter.writerow(data2)
     i=i+1

employ_data.close()