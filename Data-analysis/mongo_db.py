import pymongo
from pymongo import MongoClient
import sys


connection = MongoClient('localhost',27017)
db = connection.DataAnalysis
db.new_dooc.insert({"name":"rajan"})


