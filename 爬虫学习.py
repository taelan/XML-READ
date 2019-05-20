# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:57:39 2019

@author: 41223
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#url = 'http://soso.nipic.com/q__g_0.html'

#r = requests.get(url)
#r.text
#print(r.text)
#批量获取url
urlist = []
ui = 'https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-'
for i in [1,2,3,4]:
  u = ui + str(i)
  #print(u)
  urlist.append(u)
#print(urlist)
  
datai = []
n = 0

for ui in urlist:
    print(ui)

    #访问页面
    #u1 = urlist[0]
    r = requests.get(ui)
    soup = BeautifulSoup(r.text,'lxml')
    #print(soup.title)


    #利用ul找到所有内容,为了不引起歧义，class=>class_
    ul = soup.find('ul',class_="list_item clrfix")
    #print(ul)
    li = ul.find_all('li')
    #print(li)
    #print(li[0].text)
    
    #用字典去存储数据
    #data1 = []
    for i in li:
        n += 1
        dic = {}
    
        li1 = li[0]
        dic['景点名称: '] = i.find('span',class_="cn_tit").text
        dic['攻略数量： '] = i.find('div',class_="strategy_sum").text
        dic['评论数量： '] = i.find('div',class_="comment_sum").text
        dic['排名: '] = i.find('span',class_="ranking_sum").text
        dic['星级: '] = i.find('span',class_="total_star").find('span')['style'].split(':')[1]
        #获取标签里的属性find('span')类型['style']属性.split(':')分列[1]
        datai.append(dic)
        print('成功采集%i条数据' %n)
    
    #print(datai)
    df = pd.DataFrame(datai)
    df



