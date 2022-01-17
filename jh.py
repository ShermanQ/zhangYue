#!/usr/bin/python
import requests
import json
import time
import logging
import os
import random

logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.INFO)

bid = '11314762'
startPage=1
endPage=156

cookies = r"_9755xjdesxxd_=32; YD00000592013604:WM_TID=Ir7k8yDaC6JFBRFBFUJr+V5S7yLNPNRW; gdxidpyhxdE=s/1Vxok8xhQL4kTRWop83w0VonTJi38ZxObDz3lQlpmvxDnQfWO3t9gutBRaOI9+\fR93N5aGB9q+poDwDbg\yvQm6OxpSoCULr0n4jU+Ut9CCOR0es+/PcDA6/m0Ez+7wUXGWkfa+4LfE+2h3W4mrhEye9V3UIpN+pAt1rG/7VN\yDJ:1641771907253; YD00000592013604:WM_NI=0jL1yqafAlddjUo7slZ7WbOq+B6O6ShpYOpBDeEGotwZ04pfyRfPfGYSN/NDZIwK6yVxrxECgUVuF6WYAlIQnr3rclaaGXa7CpNuPLDI/R2jEkkDteXTK2BOjumAWQxzQUo=; YD00000592013604:WM_NIKE=9ca17ae2e6ffcda170e2e6eeacf64eba98f9d4ec73b4eb8fa2d84a928b8bafb53d9c8f98a9e470e9f5b695c82af0fea7c3b92af4b684d2fc7ba3ba8f8de770aa8ba1d8f2689ae99983ce7be99efab0b559acb097b0f34a88bb8ba8ee80b58600d5f36ebb8eaab1e54d9b8d82d0cd509a97b9acb57396a8be99c849a58b9a96c53e95878f8dcc5baeaefd93e268a3bf89b9e43d81b08296d3488897e1b3b16287b5a5a5f76f9c8c85d3c145aaaba3a2d65bbca69fb6ee37e2a3; openwapuserInfo_cff385e8=10dbVFEEAwUCCQYCAlAFDFUAAlRUBwBRUAcEV1UDCQwLTBdeUAUJF1tKeFdXUSpXAVhaRAxXD1RfRwlTDkBaS31YAw0PFghXCAgNQQgNXBoTQlEUeVRYAEYPQF4NWBFrBgFcVVQFAAcQAkUICg9ESApQQABYR1hHX0cJVA5AEQNM"

#cookies = "gdxidpyhxdE=BDAT214s24ULJ/SOrR+k2dIoX8updSASnKnocejTwCdvLEMaXn7CkPEohRmQ0dLhC/gV2qDii35XrDC/AweqIdMBmzOB\EZmlzf/2ST/8MWMT\amwC9cCgPmxPHlhyxowddMDasJ/M1sQDq0\lZrhoNBZ+r\+Osvgfly4PCcNVmh5PM8:1641516589334; _9755xjdesxxd_=32; YD00000592013604:WM_NI=PbcINmIDs0Lzgn06OXTkvw1AZgH8NUzghAh7g0Kt3zNskS2b1hJ1rf9PgDtrRBxBpGXKxP1Xbbb961Vz4xHq7AeNXGHTgTa0/AUglAx6HOC9xDeVv9/ad55zyXvTT3xyNWE=; YD00000592013604:WM_NIKE=9ca17ae2e6ffcda170e2e6ee96b321b3b7ae88eb7fb39e8ab2d85f839b9faef82587e88c93ed6f8b94acb6c72af0fea7c3b92a94beadaacd678b9cbdd1cf72a5b200d7ce5498b5ba98b44b9ab988d9cd5fbab9a8a2eb3da5f08595b2728eada5b4b16af3b886d2f16efb90a9a5f77a929eb8a3f34d9c95b8b1b454a2beaedab53b96a6fc99cb7bf59fabafdb4d8c8ca9b5e43ced9f9b88ef4bbcea88b0c233bc9cabb7f533edbfacd6b872bb88bab5d739bca782b8c837e2a3; YD00000592013604:WM_TID=Ir7k8yDaC6JFBRFBFUJr+V5S7yLNPNRW; openwapuserInfo_cff385e8=d1b0BwhVBVZRVVUDBQcCUlFXBANQBQBRBQMPClACXgYLGUANCVQPRAgWK1ZQBi0JBQ9cEwhVD1QKQwIOC0ENQX0NVF5WRw4EW1ReQA9aW0QXFVdDfVZYABMLSwMIWUZhBlQLBg1UBlRDXhYJDVhDFg4HRldcRVhHCkMCCQtBRglM"
cookie = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
while(True):
    cid = random.randint(startPage,endPage+1)
    cid = str(cid)
    url1 = 'https://s.zhangyue.com/readtimereport?bid='+bid+'&cid='+cid+'&intervalMinute=50&rentId=100815&appId=cff385e8'

    url2 = 'https://s.zhangyue.com/readtime?rentId=100815&appId=cff385e8&bookId='+bid
    
    r1 = requests.get(url1,headers=headers, cookies=cookie)
    state1=json.loads(r1.text).get('body')
    logging.info(state1)
    logging.info(cid+'------------------------')
    r2 = requests.get(url2,headers=headers, cookies=cookie)
    state2=json.loads(r2.text).get('body')
    logging.info(state2)
    time.sleep(10*60)
