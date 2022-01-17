#!/usr/bin/python
import requests
import json
import time
import logging
import os
import random

logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.INFO)

#bookid 
bid = '11314762'
#the numer of book pages
startPage=1
endPage=156

#enter your cookie
cookies =""
cookie = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
while(True):
    cid = random.randint(startPage,endPage+1)
    cid = str(cid)
    url1 = 'https://s.zhangyue.com/readtimereport?bid='+bid+'&cid='+cid+'&intervalMinute=20&rentId=100815&appId=cff385e8'

    url2 = 'https://s.zhangyue.com/readtime?rentId=100815&appId=cff385e8&bookId='+bid
    
    r1 = requests.get(url1,headers=headers, cookies=cookie)
    state1=json.loads(r1.text).get('body')
    logging.info(state1)
    logging.info(cid+'------------------------')
    r2 = requests.get(url2,headers=headers, cookies=cookie)
    state2=json.loads(r2.text).get('body')
    logging.info(state2)
    time.sleep(20*60)
