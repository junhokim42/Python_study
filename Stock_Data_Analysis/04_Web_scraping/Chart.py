import pandas as pd
krx_list = pd.read_html('C:/Users/82102/Desktop/Project/Python_study/Stock_Data_Analysis/04_Web_scraping/상장법인목록.txt')
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
print(krx_list)