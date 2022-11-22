# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:28:33 2022

@author: Sai Siddhanth
"""

from bs4 import BeautifulSoup
import requests
import pandas

URL = 'https://www.amazon.in/s?k=phones&crid=1NKQYCLM06CJ2&sprefix=phon%2Caps%2C324&ref=nb_sb_noss_2'

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0', 'Accept-Language':'en-US,en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)

#print(type(webpage.content))


soup = BeautifulSoup(webpage.content,'html.parser')

#print(type(soup()))

links = soup.findAll('a',attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

#print(links[0].get('href'))

link = links[0].get('href')

product_list = 'https://www.amazon.in' + link

#print(product_list)





new_webpage = requests.get(product_list, headers=HEADERS)

new_soup = BeautifulSoup(new_webpage.content,'html.parser')

print(new_soup.find('span',attrs= {"id":'productTitle'}).text.strip())

print(new_soup.find('span',attrs= {"class":'a-price-whole'}).text.strip())

print(new_soup.find('span',attrs= {"class":'a-icon-alt'}).text.strip())


