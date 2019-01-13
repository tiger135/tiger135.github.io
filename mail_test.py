from email.mime.text import MIMEText
from datetime import date
import smtplib
import os
import tomtom_request

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "vishakh.arora29@gmail.com"
SMTP_PASSWORD = "guitar2003"

EMAIL_TO = ["vishakh.arora29@gmail.com"]
EMAIL_FROM = "vishakh.arora29@gmail.com"
EMAIL_SUBJECT = "Fire Detected"

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

FIRESTATIONS = tomtom_request.fireStations()

DATA="Fire detected. Click the following link to see where smoke was detected: https://vishakhs-macair.local:5000/mark \nHere is a list of the top three closest firestations:\n"+str(FIRESTATIONS)
#print(DATA)

def send_email():
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()
send_email()