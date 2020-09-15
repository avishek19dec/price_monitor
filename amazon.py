import requests,re
from bs4 import BeautifulSoup

def scrape_amazon(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    price_tag = soup.find(id = "price")
    price = (price_tag.span.string)[3:]
    price = float(price.replace(",", ""))
    # print(price)
    return price