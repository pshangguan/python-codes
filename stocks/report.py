import os
import sys
import time
from datetime import datetime

datestr=datetime.strftime(datetime.now(),"%Y_%m_%d")

dailyfile=open(datestr+"_dailyquote.txt","r")

for s in dailyfile:
	s = s.split(" ")
	print("%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.5f%%\t%.2f\t%.2f\t%.5f%%" % (s[0],float(s[1]),float(s[2]),float(s[3]),float(s[4]),float(s[5])*100,float(s[6]),float(s[7]),float(s[8])*100))

dailyfile.close()

