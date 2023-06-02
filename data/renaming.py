# import os
# import datetime
# import sys
# from time import localtime, strftime
#
# original_stdout = sys.stdout
# t_date = strftime("%y%m%d", localtime())
#
# save_file = open("log_" + t_date + ".txt", "w")
# sys.stdout = save_file
#
# d_file = './kospi200_option/'
# files = os.listdir(d_file)
#
# print('폴더의 파일 : ', files)
# print('\n')
#
# for f_name in files:
#     print(f_name)
#     print('\n')
#
# for i in range(0, len(files)):
#     for j in range(0, len(files)):
#         if datetime.datetime.fromtimestamp(os.path.getctime(d_file + files[i])) < datetime.datetime.fromtimestamp(
#                 os.path.getctime(d_file + files[j])):
#             files[i], files[j] = files[j], files[i]
#
# for i in range(0, len(files)):
#     print(datetime.datetime.fromtimestamp(os.path.getmtime(d_file + files[i])), files[i])
#     print('\n')
#
# print('최신 파일 : ', files[-1])
# print('\n')
#
# for f_name in files:
#     print("%s" % f_name)
#
# sys.stdout = original_stdout
# save_file.close()

import glob, os

date_list = []
result_f = open("../crawling/date_list.txt")
for line in result_f:
    date_list.append(line[:-1])


# print(len(date_list))

files = glob.glob('./kospi200_option/*.csv')
files.sort(key=os.path.getmtime)

idx = 0
for file in files:
    os.rename(file, f'kospi200_option_{date_list[idx]}.csv')
    idx +=1

print(idx)



