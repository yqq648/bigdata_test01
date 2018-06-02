# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:17 2018
#应用其他工具包
import 包名/类名   
网络资源地址简称URL,
@author: yq
"""
import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
#网络连接,urlopen(地址).read().decode('utf-8','ignore')
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

#json(dict)格式工具包,将json字符串转换成dict
import json
data=json.loads(info)
data['main']['temp']













