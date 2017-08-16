import pymongo
import sys


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

try:
	cursor = grades.find( { "type": "homework" }) \
	               .sort( [ ("student_id", pymongo.ASCENDING), \
	               	        ( "score", pymongo.ASCENDING)])
except:
	print "Unexpected error:", sys.exc_info()[ 0]

