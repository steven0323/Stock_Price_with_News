''' 
    Author : Yu-Hsuan Tseng
    Date : 2021 /02/ 03
    Objective : The primary goal of this project is to measure how well the news relating individual company affects its stock price.
    Stock : Palantir technology
    Referred Url : https://finance.yahoo.com/quote/pltr

'''

import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import requests 
import time


class News_crawler:

    def __init__(self):
        self.url = "https://finance.yahoo.com/quote/PLTR/news?p=PLTR"
        self.url_comment="https://finance.yahoo.com/quote/PLTR/community?p=PLTR"

    def crawler(self):
        # elements of comments from url1 : <ul> <comments-list List(n) Ovs(touch) Pos(r) Mt(10px) Mstart(-12px) Pt(5px)>
        # elements of stock price : <span> <Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)">
        # elements of increase/decrease <span> <Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)>
        r = requests.get(self.url)
        r1 = requests.get(self.url_comment)
        soup = BeautifulSoup(r.content,'html.parser')
        soup1 = BeautifulSoup(r1.content,'html.parser')
        price_tag = soup.find("span",class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
        percentage = soup.find("span",class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)").text
        print(price_tag,percentage)
        comments = soup1.find("ul",class_="comments-list List(n) Ovs(touch) Pos(r) Mt(10px) Mstart(-12px) Pt(5px)").find_all("div",class_="C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)")
        
        # in order to see sentiment analysis on the overall comments
        all_content = ""
        for comment in comments: 
            all_content+=comment.text
        

if __name__=="__main__":
    
    News_crawler = News_crawler()
    #while True:
    News_crawler.crawler()
    #time.sleep(30)