import os
import time
from datetime import datetime
from pytz import timezone

def getit():
	print("In function!")

timefmt="%H:%M"
now_pdt=datetime.now(timezone('US/Eastern'))
print(now_pdt.strftime(timefmt))
cnt=0
while now_pdt.strftime(timefmt) < "13:11":
	getit()
	time.sleep(5)
	cnt = cnt + 1
	now_pdt=datetime.now(timezone('US/Eastern'))
