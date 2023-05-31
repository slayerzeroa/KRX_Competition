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
for i in range(1, 5000):
    try:
        date = datetime.datetime.now() - datetime.timedelta(days=i)

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, '//*[@id="prodId"]/option[3]').click()

        driver.implicitly_wait(20)
        driver.find_element(By.ID, "jsSearchButton").click()
        driver.implicitly_wait(20)
        if driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td').text == '데이터가 없습니다.':
            for j in range(8):
                driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(Keys.BACK_SPACE)
            driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(date.strftime("%Y%m%d"))
            driver.implicitly_wait(20)
            driver.find_element(By.ID, "jsSearchButton").click()
        else:
            driver.implicitly_wait(20)
            driver.find_element(By.XPATH, '//*[@id="MDCSTAT125_FORM"]/div[2]/div/p[2]/button[2]/img').click()
            driver.implicitly_wait(20)
            driver.find_element(By.XPATH, "//a[text()='CSV']").click()
            driver.implicitly_wait(20)
            for j in range(8):
                driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(Keys.BACK_SPACE)
            driver.find_element(By.XPATH, '//*[@id="trdDdBox1"]').send_keys(date.strftime("%Y%m%d"))
            driver.implicitly_wait(20)
            driver.find_element(By.ID, "jsSearchButton").click()
            date_list.append(date.strftime("%Y%m%d"))
    except:
        pass

with open('date_list.txt', 'w') as f:
    for item in date_list:
        f.write("%s\n" % item)


# time.sleep(4)
# for i in range(10):
#     driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div/div[2]').send_keys(Keys.PAGE_DOWN)
#
# table = driver.find_element(By.XPATH, '//*[@id="jsMdiContent"]/div/div[2]/div[1]/div[1]/div[2]/div/div/table/tbody')
# rows = table.find_elements(By.TAG_NAME, "tr")
#
# for index, value in enumerate(rows):
#     print(value.text)