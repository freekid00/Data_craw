# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
        
first='986'
se=range(1,10000)
se=list(se)
for i in range(9999):
    se[i]=str(se[i])
    if len(se[i])==1:
        se[i]=first+'000'+se[i]
    if len(se[i])==2:
        se[i]=first+'00'+se[i]
    if len(se[i])==3:
        se[i]=first+'0'+se[i]
    if len(se[i])==4:
        se[i]=first+se[i]
data_file= '/Users/zhangdi/Downloads/shunfeng.csv'
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }
base_url = 'http://www.chakd.com/sfwd/wd/sfwd{}.html'

count=1
with open(data_file,'w',newline='',encoding='utf8') as wf:
    writer = csv.writer(wf)
    for permno in se:
        print('now',permno)
        url=base_url.format(permno)
        response = requests.get(url,headers = fake_header)
        if response.status_code==200:
            response.encoding = 'GBK'
            root = BeautifulSoup(response.text,"html.parser") 
            table = root.find('table',attrs={'class':'part_tab'})
            rows = table.find_all('tr')
            for row in rows: 
                col1=root.find('th',attrs={'colspan':2})
                record=[col1.get_text().strip(),]
                columns = row.find_all('td')
                for col in columns: 
                    record.append(col.get_text().strip())
                writer.writerow(record)
                count+=1
print('total',count)
                    
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        