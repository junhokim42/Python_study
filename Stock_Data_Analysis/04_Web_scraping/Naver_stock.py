from datetime import *
import pandas as pd
from urllib import request as req
from bs4 import BeautifulSoup
import mplfinance as mpf

def read_naver(self, code, company, pages_to_fetch):
    url = f"https://finance.naver.com/item/sise_day.naver?code={code}"
    html = BeautifulSoup(req.get(url, headers = {""}).text, 'lxml')
    pgrr = html.find("td", class_ = "pgRR")
    if pgrr is None:
        return None
    s = str(pgrr.a['href']).split('=')
    lastpage = s[-1]
    df = pd.DataFrame()
    pages = min(int(lastpage), pages_to_fetch)
    for page in range(1,pages + 1):
        pg_url = '{}&page={}'.format(url, page)
        df = df.append(pd.read_html(req.get(pg_url, headers = {''}).text)[0])
        tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
        print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...')

read_naver()