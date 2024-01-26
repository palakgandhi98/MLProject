import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL Database Started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
        logging.info("Connection Eastablished",engine)
        df = pd.read_sql_query('Select * from students', con=engine)
        #df = pd.read_sql_query('Select * from students',mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex)
    