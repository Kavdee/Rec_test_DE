#!/usr/bin/env python
import pandas as pd
import sqlalchemy
import sys
import json

#connect to the database
try:
    engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database:3306/codetest")
    connection = engine.connect()
except Exception as e:
    print(str(e))
    sys.exit(0)

#import data
try:
    df=pd.read_sql("SELECT country, count(*) FROM people pe join places pl on pe.place_of_birth=pl.city group by country",connection)
    df.columns=['country','count']
    result_dict = dict(zip(df['country'],df['count']))
    with open('/data/output.json', 'w') as json_file:
        json.dump(result_dict, json_file)
except Exception as e:
    print(str(e))

