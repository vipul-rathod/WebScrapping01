import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

try:

    page=requests.get('https://www.amazon.in/Apple-iPhone-Pro-Max-256GB/product-reviews/B07XLS5796/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')

except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('ERROR FOR LINK:', url)
    print (error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('span', attrs={'class':'a-size-base'})

for i in links:

    print (i.text)
    print ("\n")