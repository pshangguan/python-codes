import os
from datetime import datetime
from pytz import timezone
from googlefinance import getQuotes
import json
import panda
import pandas_datareader.data as wb
import urllib2
import time
from yahoo_finance import Share
from pprint import pprint

timefmt="%H:%M"
now_pdt=datetime.now(timezone('US/Eastern'))
if now_pdt.strftime(timefmt) < "09:30":
	print("too early")

now=datetime.now()
currentprice=wb.DataReader('AAPL','google',datetime(now.year,now.month,now.day),datetime(now.year,now.month,now.day))
print(currentprice,now.year,now.month,now.day)

#print("<<done>>")

q=getQuotes('AAPL')
print json.dumps(getQuotes('AAPL'))

link = "http://finance.google.com/finance/info?client=ig&q="
url = link+"%s:%s" % ("NASDAQ", "AAPL")
u = urllib2.urlopen(url)
content=u.read()
print(content)
#data = json.loads(content[0:])
#info = data[0]
#print(info)
# t = str(info["elt"])    # time stamp
#l = float(info["l"])    # close price (previous trading day)
#o = float(info["op"])   # stock price in pre-market (after-hours)
#print(l)

yahoo=Share('AAPL')

print yahoo.get_prev_close()
print yahoo.get_open()
pprint(yahoo.get_historical('2017-08-03','2017-08-03'))
