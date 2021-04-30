import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

try:

    page=requests.get('https://www.cricbuzz.com')

except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('ERROR FOR LINK:', url)
    print (error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('div', attrs={'class':'cb-nws-intr'})

for i in links:

    print (i.text)
    print ("\n")