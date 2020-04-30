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

def write_one_page(writer,soup):
    for num in range(1,5):
        table=soup.find('table',attrs={'id':'listTable'+str(num)})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            for col in cols:
                record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)

def permno_craw(permno,market_type,driver,date):
    url='http://quote.eastmoney.com/f1.html?code={}&market={}'
    driver.get(url.format(permno,market_type))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    counts=soup.find('span',attrs={'class':'count'}).get_text().strip()
    if int(counts)==0:
        return [permno,'No data',0]
    else:
        data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/{}.csv'.format(permno)
        with open(data_file,'w',newline='',encoding='utf8') as wf:
            writer = csv.writer(wf)
            head_csv=['time','price','volumn']
            writer.writerow(head_csv)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            write_one_page(writer=writer,soup=soup)
            for page_number in range(2,(int(counts)+1)):
                driver.find_element_by_css_selector('[class="go"]').send_keys(str(page_number))
                driver.find_element_by_css_selector('[class="goBtn fl"]').click()
                soup = BeautifulSoup(driver.page_source, "html.parser")
                write_one_page(writer=writer,soup=soup)
            return[permno,'finished',counts]

def stock_minute(driver,stocks,date):
    results=dict()
    driver = driver
    for stock,market_type in stocks.items():
        print(stock,'starts')
        result=permno_craw(stock,market_type,driver,date)
        results[stock]=result
        time.sleep(1)
    for stock,record in results.items():
        print(stock,record)

def stock_cash(permno,driver):
    url='http://data.eastmoney.com/zjlx/{}.html'.format(str(permno))
    driver=driver
    permno=permno
    driver.get(url)
    print(permno,'url gets')
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/{}stock_cash.csv'.format(permno)
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        head_csv=['date','close_price','return','zhuli_value','zhuli_ratio',
        'chaodadan_value','chaodadan_ratio',            
        'dadan_value','dadan_ratio',
        'zhongdan_value','zhongdan_ratio',
        'xiaodan_value','xiaodan_ratio',]
        writer.writerow(head_csv)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            for col in cols:
                content=str(col.get_text().strip())
                record.append(content)
            writer.writerow(record)
    print(permno,'stock_cash finished')