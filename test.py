#coding:utf-8
import urllib.parse
from urllib import request
import re
import pymysql
import csv

#从12306获取所有的车站
url = 'https://kyfw.12306.cn/otn/resources/js/query/qss.js?station_version=1.9035'
print('Downloading')
try:
    req = request.urlopen(url)
    html = req.read().decode('utf-8')
except urllib.URLError as e:
    print('Download error:', e.reason)
    html = None

#对html处理，获取所有车站
html = html.replace('"','').replace('\n','').replace('\t','').replace(' ','').replace('varcitys={','').replace('}','')
pattern = re.compile(u',',re.S)
bands = re.split(pattern,html)

#使用count记录爬取站数
count = 0
#开始从百度百科获取车站信息
for band in bands:
    count+=1
    try:
        band = band[0:-6]
        url= u'https://baike.baidu.com/item/'+urllib.parse.quote('%s站'%band)
        req = request.urlopen(url)
        html = req.read().decode('utf-8')
    except urllib.URLError as e:
        print('Download error:', e.reason)
        html = None
#对百度百科获取的数据处理

    html=html.replace('\n','').replace('&nbsp;','')
    pattern_key = re.compile(u'<dt class="basicInfo-item name">(.*?)</dt>',re.S)
    pattern_value = re.compile(u'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
    keys = re.findall(pattern_key,html)
    values = re.findall(pattern_value,html)
    valuesnew = []
    for j in values:
        if 'a' and '/a' in j:
            pattern = re.compile(u'<a.*?>(.*?)</a>',re.S)
            j = re.findall(pattern,j)
            valuesnew.append(j)
        else:
            valuesnew.append(j)

#将获取的信息存入字典
    dictionary = dict(zip(keys,valuesnew))
    a = dictionary.keys()
    b = []
    for i in a:
        b.append(dictionary[i])

    with open('alltestdata.csv','a+')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(a)
        writer.writerow(b)
        
#判断车站是否是特等站或者一等站，并写入csv文件
    if dictionary:
        b=[]
        for k in dictionary.keys():
            if dictionary[k] == '特等站':
                b.append(band)
                b.append(dictionary[k])
                with open('filterdata.csv','a+')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(b)
            elif dictionary[k] == '一等站':
                a=list((band,dictionary[k]))
                with open('filterdata.csv','a+')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(a)
    print('第{}站抓取完毕'.format(count))
print('输出抓取完毕')    




