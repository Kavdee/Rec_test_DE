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
