# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:28:09 2021


@author: Bill
"""
import random
import time
import requests     
import parsel      
import csv        

import multiprocessing
import os

def travel_spider():
    csv_qne = open('./myapp/travel/去哪儿.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.writer(csv_qne)
    csv_writer.writerow(['地点', '短评', '出发时间', '天数','人均费用','人物','玩法','浏览量','详情页'])
    for page in range(1, 201):
        
        url = f'https://travel.qunar.com/travelbook/list.htm?page={page}&order=hot_heat'
        response = requests.get(url)
        html_data = response.text 
        selector = parsel.Selector(html_data)
       
        url_list = selector.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()
        for detail_url in url_list:
            detail_id = detail_url.replace('/youji/', '')
            detail_url = 'https://travel.qunar.com/travelbook/note/' + detail_id
           
            response_1 = requests.get(detail_url)
            
            data_html_1 = response_1.text
            
            selector_1 = parsel.Selector(data_html_1)
           
            title = selector_1.css('.b_crumb_cont *:nth-child(3)::text').get()
            # 短评
            comment = selector_1.css('.title.white::text').get()
            # 浏览量
            count = selector_1.css('.view_count::text').get()
            # 出发日期
            date = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()
            # 天数
            days = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()
            # 人均费用
            money = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howmuch > p > span.data::text').get()
            # 人物
            character = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()
            # 玩法
            play_list = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data span::text').getall()
            play = ' '.join(play_list)
            #print(title, comment, date, days, money, character, play, count, detail_url)
            csv_writer.writerow([title, comment, date, days, money, character, play, count, detail_url])
            time.sleep(random.randint(1, 2))
    csv_qne.close()






class Schedule:
    # 1. 爬蟲模块
    def getter_spider(self):
        while True:
            travel_spider()
            time.sleep(60*60*24)  # 每24小時爬取一次
     # 2.檢驗
    def data_csv(self):
        while True:
            time.sleep(60*60*2)
            path1 = './myapp/travel/去哪儿.csv'
            size1 = os.path.getsize(path1)
    
            path2='./myapp/travel/去哪儿_数分.csv'
            size2 = os.path.getsize(path2)
    
            if size1>size2:
                os.remove('./myapp/travel/去哪儿_数分.csv')
                os.rename('./myapp/travel/去哪儿.csv','./myapp/travel/去哪儿_数分.csv')	
            


    def run(self):    
        getter_spider = multiprocessing.Process(target=self.getter_spider)
        getter_spider.start()


        # CSV有資料
        if  os.path.exists("./myapp/travel/去哪儿.csv") :
            data_csv = multiprocessing.Process(target=self.data_csv)
            data_csv.start()
         

    

if __name__ == '__main__':
    work = Schedule()
    work.run()
