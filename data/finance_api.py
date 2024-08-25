from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import requests
import json
import datetime


load_dotenv()
ECOS_API = os.getenv("ECOS_API")

today = datetime.datetime.today().strftime('%Y%m%d')


def json2df(response):
    contents = response.json()['StatisticSearch']['row']
    res_df = pd.DataFrame(contents)
    return res_df


def get_interest_df(start: str, end: str=today):
    '''
    start: 시작일자 (예시) 20210101
    end: 종료일자 (예시) 20240101
    '''

    code_dict = {'콜금리':'010101000', 'CD91일':'010502000', '국고채_2년':'010195000'}

    result_df = pd.DataFrame()
    for key, value in code_dict.items():
        url = f'https://ecos.bok.or.kr/api/StatisticSearch/{ECOS_API}/json/kr/1/100000/817Y002/D/{start}/{end}/{value}'
        response = requests.get(url)
        res_df = json2df(response)
        temp_df = res_df[['TIME', 'DATA_VALUE']]
        temp_df = temp_df.set_index('TIME')
        temp_df.columns = [key]
        result_df = pd.concat([result_df, temp_df], axis=1)
    
    return result_df