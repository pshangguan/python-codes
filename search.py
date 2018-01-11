import os, sys, string
import re

import smtplib

from email.mime.text import MIMEText

def check():

	cntY = 0
	cntN = 0
	cntE = 0
	file=open("./file1.txt","r+")
	wf=open("new.txt","w")
	oStr = "yes"
	nStr="Haha"
	for line in file:
		line = line.strip()
		if line.find("yes") != -1:
			cntY += 1
		if line.find("no") != -1:
			cntN += 1
		if line == '':
			cntE += 1
		else:
			wf.write(line + "\n")
	print("Yes: %d" % cntY)
	print("No: %d" % cntN)
	print("Empty line: %d" % cntE)
	
	file.close()
	wf.close()

	s = open("new.txt").read()
	wf=open("new.txt","w")
	wf.write(s.replace(oStr,nStr))
	wf.close()
	
	os.chmod("new.txt",0777)

#	msg = MIMEText(file.read())
#	msg["Subject"] = "This is a test from Python"
#	msg["From"] = "me"
#	msg["To"] = "pshangguan@gmail.com"

#	s = smtplib.SMTP('stmp.gmail.com')
#	s.sendmail(me, [you], msg.as_string())
#	s.quit()

check()
