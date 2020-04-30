import time
from bs4 import BeautifulSoup
import csv

def craw_basic_north(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/hsgtcg/hy.html'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/Bei_cash.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['名称','涨跌幅','今日持股股票只数','今日持股市值','今日持股占板块比','今日持股占北向资金比',
                '今日增持股票只数','今日增持市值','今日增持市值增幅','今日增持占板块比','今日增持占北向资金比',
            '增持最大股市值','增持最大股占股本比','减持最大股市值','减持最大股占股本比']
        writer.writerow(record)
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
        driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys('2')
        driver.find_element_by_css_selector('[class="btn_link"]').click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
    print('craw_basic_north finished')

def craw_basic_industry_PE(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/gzfx/hylist.html'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/industry_PE.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['行业','PE(TTM)','PE(静)','市净率','PEG值','市现率',
            '市销率','平均市值(亿元)','个股数量','亏损家数']
        writer.writerow(record)
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
        driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys('2')
        driver.find_element_by_css_selector('[class="btn_link"]').click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
    print('craw_basic_industry_PE finished')

def craw_basic_industry_cash(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/bkzj/hy.html'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/industry_cash.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['名称','今日涨跌幅','今日主力净流入净额','今日主力净流入净占比',
            '今日超大单净流入净额','今日超大单净流入净占比',
            '今日大单净流入净额','今日大单净流入净占比',
            '今日中单净流入净额','今日中单净流入净占比',
            '今日小单净流入净额','今日小单净流入净占比',
            '主力净流入最大股']
        writer.writerow(record)
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
        driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys('2')
        driver.find_element_by_css_selector('[class="btn_link"]').click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
    print('craw_basic_industry_cashs finished')

def north_basic_stock(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/hsgtcg/list.html'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    page_num=int(soup.find('a',attrs={'title':'转到最后一页'}).get_text().strip())
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/Bei_stock.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['代码','名称','今日收盘价','今日涨跌幅','今日持股股数','今日持股市值','今日持股占流通股比','今日持股占总股比',
        '今日增持持股股数','今日增持持股市值','市值增幅','今日增持持股占流通股比','今日增持持股占总股比','所属板块']
        writer.writerow(record)
        table=soup.find('table',attrs={'class':'tab1'})
        rows=table.find_all('tr')
        for row in rows:
            record=[]
            cols=row.find_all('td')
            count=1
            for col in cols:
                if count==1 or count==4:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
        for number in range(2,(page_num+1)):
            driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys(str(number))
            driver.find_element_by_css_selector('[class="btn_link"]').click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            table=soup.find('table',attrs={'class':'tab1'})
            rows=table.find_all('tr')
            for row in rows:
                record=[]
                cols=row.find_all('td')
                count=1
                for col in cols:
                    if count==1 or count==4:
                        count+=1
                        continue
                    else:
                        count+=1
                        record.append(col.get_text().strip())
                if len(record)==0:
                    continue
                else:
                    writer.writerow(record)
    print('north_stock finished')

def north_basic_stock_hist(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/hsgtcg/gzcglist.html'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/Bei_hist_stock.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['日期','沪深300涨跌幅','北向增持市值','北向增持占全市场比','北向今日持股市值','北向今日持股占市场比',
        '增持最大行业市值增持','增持最大行业占板块比增加','增持最大行业占全市场比增加',
        '增持最大股市值增持','增持最大股股数增加','增持最大股占股比增加']
        writer.writerow(record)
        table=soup.find('table',attrs={'id':'table_cgls'})
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
        for number in range(2,6):
            driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys(str(number))
            driver.find_element_by_css_selector('[class="btn_link"]').click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            table=soup.find('table',attrs={'id':'table_cgls'})
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
    print('north_stock_hist finished')

def north_basic_institution_hist(date,driver):
    date=date
    driver=driver
    url='http://data.eastmoney.com/hsgtcg/InstitutionStatistics.aspx'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_file= '/Users/zhangdi/Desktop/A_share/stock_daily/'+date+'/Bei_institute_hist.csv'
    with open(data_file,'w',newline='',encoding='utf8') as wf:
        writer = csv.writer(wf)
        record=['持股日期','机构名称','持股只数','持股市值','持股市值变化-一日',
        '持股市值变化-五日','持股市值变化-十日']
        writer.writerow(record)
        table=soup.find('table',attrs={'id':'tb_jgtj'})
        rows=table.find_all('tr')
        for row in rows:
            count=1
            record=[]
            cols=row.find_all('td')
            for col in cols:
                if count==3:
                    count+=1
                    continue
                else:
                    count+=1
                    record.append(col.get_text().strip())
            if len(record)==0:
                continue
            else:
                writer.writerow(record)
        print('page 1')
        for number in range(2,5):
            driver.find_element_by_css_selector('[id="PageContgopage"]').send_keys(number)
            driver.find_element_by_css_selector('[class="btn_link"]').click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            table=soup.find('table',attrs={'id':'tb_jgtj'})
            rows=table.find_all('tr')
            for row in rows:
                count=1
                record=[]
                cols=row.find_all('td')
                for col in cols:
                    if count==3:
                        count+=1
                        continue
                    else:
                        count+=1
                        record.append(col.get_text().strip())
                if len(record)==0:
                    continue
                else:
                    writer.writerow(record)
            print('page',number)
    print('north_institution_hist finished')