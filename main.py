# scraping situs indeed

import requests
from bs4 import BeautifulSoup

keyword = 'hotels'
# location = 'london'
url = ('https://www.bhinneka.com/jual?cari=iphone')
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
    'Safari/537.36'
}
'''
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
print(type(req))
print(type(soup))
#print(soup.prettify())

produk = soup.find_all('div', {'class':'css-194yrqz'})
#produk = soup.find('a', {'class': 'product-wrapper css-puqsxn'})
print(produk)
#i=1
#for p in produk:
#    print(p)
    
