import json
import crawler
import os

FILE_NAME = "jsonData.json"


    #call this function from the track function 
    #return the appropriate response
def save(user, item , url):
    data = []
    with open(FILE_NAME,"r") as file :
        try:
            print("inside try")
            data = json.load(file)
        except json.JSONDecodeError:
            pass

    price = crawler.get_price(url)
    item_data = {"user":user,"item":item,"price":price,"url":url}
    data.append(item_data)
    print(data)
    with open(FILE_NAME,"w") as file :
        json.dump(data,file)
    return price


