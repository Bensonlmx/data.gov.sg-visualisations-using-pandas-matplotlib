import pymongo
from pymongo import MongoClient

import pandas as pd
from datetime import date, datetime, timedelta
from dateutil.parser import parse

df = pd.read_csv("/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/CA2/rate-of-re-entry-into-employment-by-educational-attainment-quarterly.csv")
user,pw, host,db = 'root','password','127.0.0.1','myDB'

client = MongoClient()
db = client.ca2
collection = db.ca2

for index, col in df.iterrows():
    quarter = col[0]
    education1 = col[1]
    reentry_rate = col[2]
   
    
    collection.insert_one({"quarter":col[0], "education1":col[1], "reentry_rate":col[2]})
    print("Adding row" + str(index))
