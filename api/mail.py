#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import conf

from email.mime.text import MIMEText

def send_mail(title, subject, email, to):
    msg = MIMEText(title)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to

    s = smtplib.SMTP(conf.mail['server'], conf.mail['port'])

    s.login(conf.mail['login'], conf.mail['password'])
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()