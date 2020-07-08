from bs4 import BeautifulSoup
import requests
import codecs
import json
import time

list = {
    "Berlin 2019 Legends Autograph Capsule" : "176079684",
    "Berlin 2019 Returning Challengers Autograph Capsule": "176079729",
    "Mann Co. Supply Crate Key" : "1",
    "Glove Case" : "175854202",
    "Clutch Case" : "175966708",
    "Prisma 2 Case" : "176118270",
    "Shattered Web Case" : "176096390",
    "Operation Breakout Weapon Case" : "14962905",
    "Gamma 2 Case" : "165027636",
    "Danger Zone Case" : "176024744",
    "Spectrum Case" : "175880240",
    "CS20 Case" : "176091756"
}


name = input("Enter name of the case: ")
item_id = list[name]

while True:
    # you should get the item id from the network page 

    r = requests.get('https://steamcommunity.com/market/itemordersactivity?country=KZ&language=english&currency=1&item_nameid=' + item_id + '&two_factor=0')
    data = r.json()
    string = str(data['activity'])
    string = string[:-2]
    string = string[2:]
    source = string
    soup =  BeautifulSoup(source, 'lxml')
    for i, j in zip(soup.find_all("span", class_="market_ticker_name"), soup.find_all('img')):
        with open("steam.txt", 'a', encoding='utf8') as f:
            f.write(j['src'] + '-' + i.text + '\n')      
