import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glob

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing

from statsmodels.tsa.stattools import coint

from scipy import stats
import bs4 as bs
import requests
import yfinance as yf
import datetime

# resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# soup = bs.BeautifulSoup(resp.text, 'lxml')
# table = soup.find('table', {'class': 'wikitable sortable'})
tickers = pd.read_csv("tickers_small.csv")
tickers = tickers["Ticker"].values.tolist()
# print(tickers)

# tickers = ['ABT', "PAYC", "XYL","CDNS","BK","ABBV","GD","QCLN","BTBT","ETSY","AMD","QCOM"
# ,"TXN","SMH","QRVO","INTC","SOXL","BB","SNDL","RMO","WISH","OPEN","SPCE","CURI"
# ,"REGN","Z","DOCU","NNDM","PTON","FSLY","CRSP","SKLZ","PLTR","ZS","OKTA","TWLO","EH","DAO"
# ,"TAL","RLX","TME","KWEB","TSP","EDU","UVXY","SQQQ","QQQ"
# ,"IWM","UA","TCEHY","YANG","LI","SHOP","IBKR","FXI","TWTR","SOFI","NRG"
# ,"GS","TDOC","TSM","JD","SPY","WMT","GM","AAPL","XPEV","VLO","BIIB","U","PDD","BILI","NVDA","BEKE","FTCH"
# ,"COIN","SWKS","MCD","GOOG","SQ","ROKU","AMZN","CHWY","PYPL","MU","LRCX","FB","AMAT","ASML","BA",
# "SNAP","FUTU","JPM","BIDU","NIO","TIGR","HOFV","TSLA","AQB","AMC","GME","SE","C","ARKK","BABA"
# ]

# for row in table.findAll('tr')[1:]:
#     ticker = row.findAll('td')[0].text
#     tickers.append(ticker)

# tickers = [s.replace('\n', '') for s in tickers]
start = datetime.datetime(2021, 8, 31)
end = datetime.datetime(2022, 1, 3)
# data = yf.download(tickers, start=start, end=end)
# data_df = data_df.stack(data)
# data_all = []
for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)
    # data_all.append(data)
    data["Market Cap"] = np.nan
    data.drop('Adj Close', axis='columns', inplace=True)
    data_reverse = data.iloc[::-1]
    data_reverse.to_csv("/Tom-Demark-Indicator-master/Data/" + ticker + ".csv")

# print(data)
# data_df
# data_all = pd.concat(data_all)
# from datetime import date
# today = str(date.today())

# appended_data = []
# for infile in glob.glob("/Tom-Demark-Indicator-master/Data/*.csv"):
#     data = pd.read_csv(infile)
#     # store DataFrame in list
#     appended_data.append(data)
# # see pd.concat documentation for more info
# appended_data = pd.concat(appended_data)
# appended_data_reverse = appended_data.iloc[::-1]
# # write DataFrame to an excel sheet
# appended_data_reverse.to_csv("/Tom-Demark-Indicator-master/appended.csv", index=False)