import smtplib
import sys
import syslog
import re

def sendemail(msg):
	fromaddr = '**********@gmail.com'
	toaddr = '***************@gmail.com'
	username = '**********'
	password = '************'

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.set_debuglevel(1)	
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddr,  "dansguardian\n" + msg.strip() )
	server.quit()

def testLine(line, out_file):
	result = re.findall(r'DENIED', line)
	if result:
		sendemail(line)
		syslog.syslog('sent an email')
	else:
		out_file += "\n"  +line;
			
input_file = file('/var/log/dansguardian/access.log','r')
oldFile = ""
for line in input_file.readlines():
	testLine(line, oldFile)	

input_file.close()
out_file = file('/var/log/dansguardian/access.log','w')
out_file.write(oldFile)
out_file.close()		
		
