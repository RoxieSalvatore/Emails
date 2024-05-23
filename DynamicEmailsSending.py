import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'It was not me'
email['to'] = 'emailaddress'
email['subject'] = '$1000'

email.set_content(html.substitute(name = 'TinTin'),'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('some_gmail', 'gcjl qkbq qeaw ketz')
	smtp.send_message(email)
	print('all good boss!')
