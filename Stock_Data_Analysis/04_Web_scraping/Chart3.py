import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = 'https://finance.naver.com/item/sise_day.naver?code=035420&page=1'
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    print(html)
    pgrr = html.find('td', class_ = 'pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.naver?code=035420'
for page in range(1, int(last_page)+1):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(page_url, header=0)[0])

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_value(by='날짜')

plt.title('Naver (close)')
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'], 'co-')
plt.grid(color = 'gray', linestyle = '--')
plt.show()