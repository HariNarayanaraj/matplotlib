import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import style
from pandas_datareader import data as pdr

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2021, 12, 30)

tesla = pdr.DataReader('TSLA', 'yahoo', start, end)
google = pdr.DataReader('GOOG', 'yahoo', start, end)

style.use('ggplot')
tesla['Close'].plot(figsize=(30, 30), label='Tesla')
google['Close'].plot(figsize=(30, 30), label='Google')

plt.title('Tesla VS Google')
plt.legend(loc='lower right')
plt.ylabel('Price in USD', fontsize=15)
plt.xlabel('Date and time', fontsize=15)
plt.show()
