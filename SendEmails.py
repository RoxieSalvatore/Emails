import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'It was not me'
email['to'] = 'email'
email['subject'] = '$1000'

email.set_content('i am a python master')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('some_gmail', 'gcjl qkbq qeaw ketz')
	smtp.send_message(email)
	print('all good boss!')
