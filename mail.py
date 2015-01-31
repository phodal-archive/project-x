import smtplib
import conf

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hi, Phodal"
msg['From'] = "mo@xuntayizhan.com"
msg['To'] = ""

s = smtplib.SMTP(conf.mail['server'], conf.mail['port'])

s.login(conf.mail['login'], conf.mail['password'])
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
