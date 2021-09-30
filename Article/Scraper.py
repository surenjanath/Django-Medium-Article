import requests
from bs4 import BeautifulSoup as bs

def Scraper():
    pass



url     = 'https://surenjanath.medium.com/'
header  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

r = requests.get(url,headers=header)
if r.status_code == 200 :
    print(r.content)
else:
    print(r.status_code)
