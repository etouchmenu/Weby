import smtplib
# import sys, os
import urllib
import datetime
import traceback
# from email.mime.text import MIMEText
# from __future__ import print_function

from config import USERNAME, SERVER, PASSWORD, WEBSITE  #config.py need to be in the same directory
from userlist import RECEPIENT


def currTime():
    # ct = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return str(datetime.datetime.now()).split('.')[0]+" "


def botName():
        return "[Weby]: "


def sendEmail():
    #load the server login info
    FROM = USERNAME
    TO = RECEPIENT  # must be a list
    SUBJECT = "WebSite Status - Down"
    TEXT = "Weby: " + currTime() + "The website is down, please contact the site administrator."

    # Prepare actual message
    print >> log, currTime() + " preparing message to be sent"

    message = """\
    From: %s
    To: %s
    \t
    Subject: %s
    \r\n
    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    print >> log, message
    # Send the mail
    # server = smtplib.SMTP(SERVER, 587)
    # print >> log, currTime() + "connected"

    try:
        server.set_debuglevel(1)
        print >> log, server.ehlo()
        print >> log, server.starttls()
        print >> log, server.ehlo()
        print >> log, server.login(USERNAME, PASSWORD)
        # print >> log, server.sendmail(FROM, TO, message)
        # print >> log, server.quit()
    except Exception:
        print >> log, traceback.format_exc()

log = open('./status.log', 'a+')
print >> log,  "=========================="+botName() + "Start =========================="


print >> log, currTime() + ' Hi There, I\'m ' + botName() + ' and I will be checking if you site is still up '
print >> log, currTime() + botName() + 'Checking Head response... '

resp = urllib.urlopen("http://www.etouchmenu.com").getcode()
if resp != 200:
    print >> log, currTime() + botName() + "Error: site ("+WEBSITE+") responded with " + str(resp)
else:
    print >> log, currTime() + botName() + "site ("+WEBSITE+") responded "+str(resp)
    from splinter import Browser
    browser = Browser()
    browser.visit(WEBSITE)

    if browser.title == 'eTouchMenuasdfasdf - Digital asdfasfTable-Top Menus':
        print >> log, currTime() + botName() + "Yes, the official website was found!"
        browser.quit()
    else:
        print >> log, currTime() + botName() + "Error The site is down"
        browser.quit()
        sendEmail()

print >> log,  "=========================="+botName() + "Done ==========================\n\r"
