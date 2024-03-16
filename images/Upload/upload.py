#!/usr/bin/env python
import pandas as pd
import sqlalchemy
import sys

#connect to the database
try:
    engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database:3306/codetest")
    connection = engine.connect()
    print("siker")
except Exception as e:
    print(str(e))
    sys.exit(0)

#import data
try:
    people_df=pd.read_csv("/data/people.csv",index_col=False)
    places_df=pd.read_csv("/data/places.csv",index_col=False)
except Exception as e:
    print(str(e))

#load data
try:
    people_df.to_sql("people",con=engine,if_exists='append',index=False)
    places_df.to_sql("places",con=engine,if_exists='append',index=False)
    print("Data is loaded")
except Exception as e:
    print(str(e))
