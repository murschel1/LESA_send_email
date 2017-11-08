#!/usr/bin/env python

import smtplib
import fileinput

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("lesalogs","Give_Me_Logs")

#logfile = "/home/pi/Desktop/temptest.txt"
logfile = "/home/pi/Desktop/TempLog.txt"

f = open(logfile,"r")
lines = f.readlines()

body = ''.join(lines)

#print body

server.sendmail("lesalogs@gmail.com", "lesalogs@gmail.com", body)
server.quit()

f.close()

f = open(logfile,"w")
f.write('start' + '\n')
f.close()




