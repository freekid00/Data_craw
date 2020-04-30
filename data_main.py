from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from craw_basic import craw_basic_north,craw_basic_industry_PE,craw_basic_industry_cash,north_basic_stock,north_basic_stock_hist
from craw_basic import north_basic_institution_hist
from stock_minute import write_one_page,permno_craw,stock_minute,stock_cash

# stocks={
#         '603799':'1',
#         '002156':'2',
#         '002463':'2',
#         '000001':'2',
#         '600585':'1',
#         '002050':'2',
#         '601633':'1',
#         '002081':'2',
#         '002789':'2',
#         '000568':'2',
#         '000858':'2'
#         }

stocks=['300319','000063','300397','002463','600745','000625',
'000066','601633','002594','600585','603799','002463','002050',
'002081','601318','000858','000568']

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome()#chrome_options=chrome_options)
# date='2020-03-03'
for permno in stocks:
    stock_cash(permno,driver)
#north_basic_institution_hist(date,driver)
# north_basic_stock_hist(date,driver)
# time.sleep(1)
# north_basic_stock(date,driver)
# time.sleep(1)
# craw_basic_north(date,driver)
# time.sleep(1)
# craw_basic_industry_PE(date,driver)
# time.sleep(1)
# craw_basic_industry_cash(date,driver)
#time.sleep(1)
# stock_minute(driver,stocks,date)
