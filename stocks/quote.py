import os
import re
import time
from datetime import datetime
from pytz import timezone
from googlefinance import getQuotes
import json
import panda
import pandas_datareader.data as wb
import urllib2
import socket
from yahoo_finance import Share

### Define functions ###

def makefile():
	# Create the daily quote file
	stocks=open("./symbols.txt","r")
	for s in stocks:
		s=s.replace("\n","")
		p = Share(s)
		pc = (p.get_prev_close())
		new_s=s + " " + str(pc) + " 0 0 0 0 0 0 0\n"
		dailyfile.write(new_s)
	stocks.close()

def find_symbol(sym,string):
    if re.search(r"\b" + re.escape(sym) + r"\b",l):
        return True
    else:
        return False

def find_prev_closing_price(sym):
	p= Share(sym)
	return p.get_prev_close()

def get_quote(sy):
	# Use google finance for now 
	link = "http://finance.google.com/finance/info?client=ig&q="
	url = link+"%s" % (sy)
	u = urllib2.urlopen(url,timeout=20)
	content=u.read()
	data = json.loads(content[3:])
	info = data[0]
	return(float(info["l"]))

def get_new_price():
	dailyfile=open(datestr+"_dailyquote.txt","r")
	tmpfile=open("tmp.txt","w")
	for s in dailyfile:
		s=s.replace("\n","")
		s=s.split(" ")
		sym=s[0]
		prev=s[1]
		low=s[2]
		high=s[3]
		q = get_quote(sym)
		print("%5s, %8.2f" % (sym,q))
		if float(low) == 0:
			s[2] = str(q)
		if float(low) > q:
			s[2]=str(q)
		if float(high) < q:
			s[3]=str(q)
		s[4] = str(float(s[3])-float(s[1]))
		s[5] = str(float(s[4])/float(prev))
		s[6] = str(q)
		s[7] = str(q - float(prev))
		s[8] = str(float(s[7])/float(prev))
		s=' '.join(s)
		tmpfile.write("%s\n" % s)

	tmpfile.close()
	dailyfile.close()
	os.rename("tmp.txt",datestr+"_dailyquote.txt")
 
### Main ###

# Run the program only after the market is open at 9:30am ET
timefmt="%H:%M"
now_pdt=datetime.now(timezone('US/Eastern'))
if now_pdt.strftime(timefmt) < "09:30":
	print("too early")

socket.setdefaulttimeout(30)

# Create daily quote file if it does not exist yet
datestr=datetime.strftime(datetime.now(),"%Y_%m_%d")
if not os.path.exists(datestr+"_dailyquote.txt"):
	dailyfile=open(datestr+"_dailyquote.txt","w")
	makefile()
else:
	# Sync the existing daily file with symbol file
	with open('./symbols.txt','r') as sy:
		for s in sy:
			s = s.replace("\n","")
			with open(datestr+"_dailyquote.txt", 'r') as fh:
			    for l in fh:
				if find_symbol(s,l):
					break
			    else:
				print("add new symbol %s" % s)
				new_s=s + " " + find_prev_closing_price(s) + " 0 0 0 0 0 0 0\n"			
				fh = open(datestr+"_dailyquote.txt", 'ab')
				fh.write(new_s)
			fh.close()
get_new_price()

while now_pdt.strftime(timefmt) < "16:01":
	get_new_price()
	time.sleep(30)
	now_pdt=datetime.now(timezone('US/Eastern'))

print("<<done>>")

### End ###
