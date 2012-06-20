#!/usr/bin/python
import smtplib
import sys
import syslog
import re

from_email_pattern = re.compile('From: ([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
to_email_pattern = re.compile('To: ([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')

def sendemail(msg, fromaddr, toaddr):
	username = '**********'
	password = ''

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.set_debuglevel(1)
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddr,msg)
	server.quit()

if __name__ == "__main__":
   email = sys.stdin.read()
   sender = from_email_pattern.match(email)
   recp = to_email_pattern.match(email)
   sendemail(email, sender, recp)
