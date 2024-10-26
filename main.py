import pandas as pd
from data import wvkospi, db
import datetime



def main():
    t = (datetime.datetime.now() - datetime.timedelta(days=2)).date()
    underlying, target = wvkospi.get_wvkospi(t=t)
    df = pd.DataFrame({'BAS_DD': [t.strftime('%Y%m%d')], 'KOSPI': [underlying], 'WVKOSPI': [target]})
    db.update_wvkospi(df)





start = datetime.datetime(2023, 8, 1).date()

while start <= datetime.datetime.now().date():
    try:
        underlying, target = wvkospi.get_wvkospi(t=start)
        df = pd.DataFrame({'BAS_DD': [start.strftime('%Y%m%d')], 'KOSPI': [underlying], 'WVKOSPI': [target]})
        db.update_wvkospi(df)
        start += datetime.timedelta(days=1)
    except Exception as e:
        print(e)
        start += datetime.timedelta(days=1)
        continue