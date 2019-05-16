# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:00:53 2019

@author: 41223
"""

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd


DomTree = xml.dom.minidom.parse(r'C:\Users\41223\课件\XSJL26.xml')

collection = DomTree.documentElement
#print ('nodeName:', collection.nodeName)        #每一个结点都有它的nodeName，nodeValue，nodeType属性
#print ('nodeValue:', collection.nodeValue )     #nodeValue是结点的值，只对文本结点有效
#print ('nodeType:', collection.nodeType)
#print ('ELEMENT_NODE:', collection.ELEMENT_NODE)

if collection.hasAttribute('shelf'):
    
   print( 'Root element : %s' % collection.getAttribute('shelf'))
   
Tickets = collection.getElementsByTagName('TICKET')

df_dict = {}
ZF_list = []
PJXX_list = []
for TICKET in Tickets:
    #print('——----------------——')
    if TICKET.hasAttribute('JLBH'):
        bh = TICKET.getAttribute('JLBH')
        #print('JLBH: ' + bh)
          
        Payments = TICKET.getElementsByTagName('Payment')
        zf_list = []
        for Payment in Payments:           
            if Payment.hasAttribute('NAME'):
                zffs = Payment.getAttribute('NAME')
                zf_list.append(zffs)
                #print('Payment: ' + zffs)       
        #print(zf_list)        
                
        Items = TICKET.getElementsByTagName('Item')
        
        pjxx_list = []
        for Item in Items:
          #if Item.hasAtturibute('Item'):

          NAME = Item.getElementsByTagName('NAME')[0]
          name = NAME.childNodes[0].data
          #print ('NAME: ' + name)
          #print ("NAME: %s" % NAME.childNodes[0].data)
          XSSL = Item.getElementsByTagName('XSSL')[0]
          xssl = XSSL.childNodes[0].data
          #print ('XSSL: ' + xssl)
          #print ("XSSL: %s" % XSSL.childNodes[0].data)
          Price = Item.getElementsByTagName('Price')[0]
          price = Price.childNodes[0].data
          #print ('Price: ' + price)
          #print ("Price: %s" % Price.childNodes[0].data)
          XSJE = Item.getElementsByTagName('XSJE')[0]
          xsje = XSJE.childNodes[0].data
          #print ('XSJE: ' + xsje)
          pjxx = [name,xssl,price,xsje,]
          #print(SPXX)
          pjxx_list.append(pjxx)
        #print(pjxx_list)
    ZF_list.append(zf_list) 
    PJXX_list.append(pjxx_list)
    df_dict = {'支付方式： ':ZF_list,'票据信息: ':PJXX_list }
        
print(df_dict) 
df = pd.DataFrame(df_dict)
df.to_excel(r'C:\Users\41223\Desktop\纪念品商店\五一销售数据.xlsx',index=False)   
          #print ("XSJE: %s" % XSJE.childNodes[0].data)
#with pd.ExcelWriter('new.xls') as Writer:
    #df.to_excel(Writer,'Sheet1',index=False)        
            
