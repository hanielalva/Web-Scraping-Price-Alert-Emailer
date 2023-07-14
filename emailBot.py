import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ae/Sony-Playstation-Console-Standard-International/dp/B08FC5L3RG/ref=sr_1_2?crid=2BR44AENUBT7V&keywords='
+'ps5&qid=1689235254&sprefix=ps5%2Caps%2C276&sr=8-2&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def get_price():

    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_element = soup.find('span', {'class': 'a-price-whole'}).get_text().strip()
    price_number = float(price_element.replace(",", ""))
    print(price_number)
    if (price_number < 1400):
        send_mail()

def send_mail():
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.ehlo()
    email.login('#########your_email@gmail.com', '#############your_app_password')
    email.sendmail('#########your_emailgmail.com', '#########your_email@gmail.com', 'Subject: WOOO THE PS5 IS CHEAP \n\n'
                   + ' Look up the PS5 on amazon right now!!!\n{URL}')
    print('price update email sent')
    email.quit()

get_price()
# utlilze import time.sleep for the loop to keep repeating