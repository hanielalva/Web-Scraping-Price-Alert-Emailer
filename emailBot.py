import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ae/Sony-Playstation-Console-Standard-International/dp/B08FC5L3RG/ref=sr_1_2?crid=2BR44AENUBT7V&keywords=ps5&qid=1689235254&sprefix=ps5%2Caps%2C276&sr=8-2&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def getPrice():

    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    priceElement = soup.find('span', {'class': 'a-price-whole'}).get_text().strip()
    priceNumber = float(priceElement.replace(",", ""))
    return priceNumber

# utlilze import time.sleep for the loop to keep repeating