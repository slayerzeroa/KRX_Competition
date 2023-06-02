import datetime
import glob, os

import pandas as pd
import matplotlib.pyplot as plt

def cal_week(date):
    return datetime.date.weekday(datetime.datetime.strptime(date, '%Y%m%d'))

files = glob.glob('../data/kospi200_option/*.csv')

print(files)

# file_name = files[0].split('/')[-1].split('.')[0][-8:]

volume_dict = {}

for file in files:
    df = pd.read_csv(file, encoding='cp949')
    total_volume = df[df['거래량'] != 0.0]['거래량'].sum()
    file_date = file.split('/')[-1].split('.')[0][-8:]
    volume_dict[file_date] = total_volume

print(volume_dict)

week_volume = [0, 0, 0, 0, 0, 0, 0]

for key, value in volume_dict.items():
    week_volume[cal_week(key)] += value

print(week_volume)

plt.bar(['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat', 'Sun'], week_volume)
plt.show()

volume_dict = {}
for file in files:
    df = pd.read_csv(file, encoding='cp949')
    total_volume = df[df['거래량'] != 0.0]['거래량'].sum()
    file_date = file.split('/')[-1].split('.')[0][-8:]
    volume_dict[file_date] = total_volume

# 리스트 정리
monthly_volume = []
monthly_set = set()
for key, value in volume_dict.items():
    monthly_set.add(key[0:6])

monthly_name_list = list(monthly_set)
monthly_name_list.sort()

print(monthly_name_list)

monthly_dict = {}
for i in monthly_name_list:
    monthly_dict[i] = 0

for key, value in volume_dict.items():
    if cal_week(key) == 3:
        monthly_dict[key[0:6]] += value

print(monthly_dict)

plt.bar(monthly_name_list, monthly_dict.values())
plt.show()