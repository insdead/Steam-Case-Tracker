from bs4 import BeautifulSoup
import requests
import codecs
import json
import time
session_id = 'f05efa82aeca03709d656ccd'
headers = {
    'Host': 'steamcommunity.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://steamcommunity.com/search/users/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Cookie': 'timezoneOffset=21600,0; _ga=GA1.2.1502511340.1592201903; _gid=GA1.2.78180794.1594181359; strInventoryLastContext=730_2; sessionid=' + session_id + '; steamCountry=KZ%7Cf23b2f5129a6693b37d04d64b676badd'
}

# for itera in main_result:

user_name = input("Enter a name of the user ")

r = requests.get('https://steamcommunity.com/search/SearchCommunityAjax?text=' + user_name +'&filter=users&sessionid=' + session_id + '&steamid_user=false&page=1', headers=headers)
data = r.json()
string = str(data['html'])
string = string[:-2]
string = string[2:]
source = string
soup =  BeautifulSoup(source, 'lxml')
for i, j in zip(soup.find_all('img'), soup.find_all('a', href=True)):
    with open("result.txt", 'a', encoding='utf8') as f:
        f.write(j['href'] + '-' + i['src'] + '\n')      

replace = "https://steamcdn-a.akamaihd.net"
to_replace = "https://cdn.cloudflare.steamstatic.com"

with open('result.txt', 'r') as file :
    filedata = file.read()
    filedata = filedata.replace(replace, to_replace)
    with open('result.txt', 'w') as file:
        file.write(filedata)