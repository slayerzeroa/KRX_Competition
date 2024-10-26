import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

import os
import pymysql

import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler


load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')
table_name = os.getenv('TABLE_NAME')

# DB 정보 불러오기

def get_wvkospi():
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{db_port}/{db_name}?charset=utf8mb4")
    query = f"select * from {table_name}"
    df = pd.read_sql(query, engine)
    return df


df = get_wvkospi()

# 정규화
scaler = MinMaxScaler()
scaler.fit(df[['KOSPI', 'WVKOSPI']])
df[['KOSPI', 'WVKOSPI']] = scaler.transform(df[['KOSPI', 'WVKOSPI']])

plt.plot(df['BAS_DD'], df['KOSPI'], label='KOSPI')
plt.plot(df['BAS_DD'], df['WVKOSPI'], label='WVKOSPI')

plt.legend()
plt.show()