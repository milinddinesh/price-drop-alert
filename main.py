#! /usr/bin/env python3

import requests as r
from bs4 import BeautifulSoup
import fun
import re
import time

URL = "https://www.amazon.in/Oneplus-Obsidian-Bluetooth-Wireless-Cancellation/dp/B07XWBJ9L1/ref=sr_1_3?keywords=oneplus+buds+z2&qid=1680583663&sprefix=oneplus+buds+%2Caps%2C554&sr=8-3"
initial_price = 4950
headers = {'User-Agent': fun.GET_UA()}

while True:
    page = r.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    span = fun.get_price(soup)
    result = 0
    if span:
        price = span[0].text
        print(price)
        match = re.search(r"₹([0-9,]+)\.\d{2}", price)
        print(match)

    if result < initial_price:
        print("price dropped")
        time.sleep(5)
        break
    else : 
        print(result)
        continue