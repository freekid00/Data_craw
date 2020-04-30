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

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
url='http://data.eastmoney.com/cjsj/hyzs_list_EMI01523157.html'
driver.get(url)
data_file='/Users/zhangdi/Desktop/A_share/stock_daily/house_sales.csv'
soup=BeautifulSoup(driver.page_source,'html.parser')
with open(data_file,'w',newline='',encoding='utf8') as wf:
    writer = csv.writer(wf)
    head_csv=['date','index','rate']
    writer.writerow(head_csv)
    table=soup.find('table',attrs={'id':'table'})
    rows=table.find_all('tr')
    for row in rows:
        record=[]
        count=1
        cols=row.find_all('td')
        for col in cols:
            if count>3:
                break
            else:
                count+=1
                record.append(col.get_text().strip())
        writer.writerow(record)
    print('page 1')
    for num in range(2,30):
        driver.find_element_by_css_selector('[id="tablePagegopage"]').send_keys(num)
        driver.find_element_by_css_selector('[class="btn_link"]').click()
        soup=BeautifulSoup(driver.page_source,'html.parser')
        table=soup.find('table',attrs={'id':'table'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            count=1
            cols=row.find_all('td')
            for col in cols:
                if count>3:
                    break
                else:
                    count+=1
                    record.append(col.get_text().strip())
            writer.writerow(record)
        print('page',num)
print('finished')