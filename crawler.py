#! /usr/bin/env python3

import requests as r
from bs4 import BeautifulSoup
import re
import random

#update these dicts if price cannot be rertieved 
amazon = {"span":{"class": "a-offscreen"}}
flipkart = {} #to be added later 

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
    return random.choice(uastrings)

#this function needs to be updated to add flipkart urls
def get_price(url):
    headers = {'User-Agent': GET_UA()}
    page = r.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    for key in amazon : 
        span = soup.find_all(key,amazon[key])
        if span:
            price = span[0].text
            match = re.search(r"₹([0-9,]+)\.\d{2}", price)
            return match.group(1)
        else: return False


# https://www.amazon.in/Oneplus-Obsidian-Bluetooth-Wireless-Cancellation/dp/B07XWBJ9L1/ref=sr_1_3?keywords=oneplus+buds+z2&qid=1680583663&sprefix=oneplus+buds+%2Caps%2C554&sr=8-3
# initial_price = 4950


# while True:
#     result = 0


#     if result < initial_price:
#         print("price dropped")
#         time.sleep(5)
#         break
#     else : 
#         print(result)
#         continue