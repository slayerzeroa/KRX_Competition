## selenium, webdriver 설치 확인
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import datetime


url = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201050101"

driver = wb.Chrome()
driver.get(url)

date_list = []

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//*[@id="prodId"]/option[4]').click()

driver.implicitly_wait(20)
driver.find_element(By.ID, "jsSearchButton").click()
driver.implicitly_wait(20)
idx = 0
for i in range(0, 2000):
    try:
        date = datetime.datetime.now() - datetime.timedelta(days=i)
        for j in range(8):
            driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(Keys.BACK_SPACE)
        driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(date.strftime("%Y%m%d"))
        driver.implicitly_wait(20)
        driver.find_element(By.ID, "jsSearchButton").click()

        if driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td').text == '데이터가 없습니다.':
            pass
        else:
            date_list.append(date.strftime("%Y%m%d"))
            driver.implicitly_wait(20)
            driver.find_element(By.XPATH, '//*[@id="MDCSTAT125_FORM"]/div[2]/div/p[2]/button[2]/img').click()
            driver.implicitly_wait(20)
            driver.find_element(By.XPATH, "//a[text()='CSV']").click()
            driver.implicitly_wait(20)
            idx+=1
    except:
        pass

with open('date_list.txt', 'w') as f:
    for item in date_list:
        f.write("%s\n" % item)

print(len(date_list))
print(idx)

# time.sleep(4)
# for i in range(10):
#     driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div/div[2]').send_keys(Keys.PAGE_DOWN)
#
# table = driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div/div[2]/div[1]/div[1]/div[2]/div/div/table/tbody')
# rows = table.find_elements(By.TAG_NAME, "tr")
#
# for index, value in enumerate(rows):
#     print(value.text)