import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input('Input the URL of the amazon product you wish to check every day: ')
comparison_price = input('Input the price at which if the product is lower than it, you would want to be emailed (it will be checked daily): ')
sender_gmail = input('Input the Gmail you want to send the update with: ')
sender_password = input('Input the app password of that Gmail to send with: ')
receiver_gmail = input('Input the Gmail you want to be notified at: ')
custom_message = input('Input an optional message in the email: ')
frequency_to_check = int(input('Input the number of days to check: '))



def price_comparer():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_element = soup.find('span', {'class': 'a-price-whole'}).get_text().strip()
    price_number = float(price_element.replace(",", ""))
    print('Current price: ', price_number)
    if (price_number < float(comparison_price)):
        send_mail()
        return True
    return False

def send_mail():
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.ehlo()
    email.login(sender_gmail, sender_password)
    email.sendmail(sender_gmail, receiver_gmail, 'Subject: The amazon product\'s price is below what you desire! \n\n'
                   + ' Look up the product on amazon right now!!!\n'+custom_message+'\n'+URL)
    print('price update email sent')
    email.quit()

for i in range(0,frequency_to_check):
    stop_checking = price_comparer()
    if (stop_checking):
        break
    print("Day "+i+" is over")
    time.sleep(3600*24)