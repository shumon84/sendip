#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
import codecs
import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formatdate

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    password = raw_input()
    smtpobj.login(from_addr, password)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    sys.stdout = codecs.getwriter('utf8')(sys.stdout)

    html = urllib2.urlopen("http://ipecho.net")
    soup = BeautifulSoup(html,"html.parser")
    ip = soup.body.main.div.h1.string.split(" ")[3]

    addr = sys.argv[1]
    subject = '[%s]' % os.uname()[1] + 'グローバルIPアドレス'
    body = ip

    msg = create_message(addr, addr, subject, body)
    send(addr, addr, msg)
