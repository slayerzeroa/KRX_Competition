import datetime



for i in range(100):
    date = datetime.datetime.now() - datetime.timedelta(days=i)
    print(date.strftime("%Y%m%d"))