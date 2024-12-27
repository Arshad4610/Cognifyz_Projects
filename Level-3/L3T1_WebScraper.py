# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:18:30 2024

@author: rawqa
"""
import requests
from bs4 import BeautifulSoup
def webscraper(url):
    res=requests.get(url)
    if(res.status_code==200):
        soup=BeautifulSoup(res.content,"html.parser")
        headings=soup.find_all(['h1','h2','h3','h4'])
        for i in headings:
            print(f"Heading: {i.get_text()}")
        links=soup.find_all('a',href=True)
        for i in links:
            print(f"Link:{i.get('href')}-{i.get_text()}")
    else:
        print(f"failed to retrieve the web page. Status code: {res.status_code}")
    
    
    
    
url="https://www.flipkart.com/?affid=affveve&affExtParam1=75679644a43eb95113b13808822b4ffa&affExtParam2=60827"
webscraper(url)