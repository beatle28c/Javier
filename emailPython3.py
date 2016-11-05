# Import smtplib for the actual sending function
import smtplib
import sys
import os
from picamera import PiCamera
from time import sleep

# Here are the email package modules we'll need
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Se ha abierto el Garage'
me ="jcamposr28c@gmail.com"
family = "nautilus28c@gmail.com"
password = "rubiks+08"
msg['From'] = me
msg['To'] = family

# Assume we know that the image files are all in PNG format
body = 'Alguien ha abierto el garage, se agrega una imagen del vehiculo'
msg.attach(MIMEText(body, 'plain'))
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Fotos/image.jpg')
camera.stop_preview()

filename = "image.jpg"
attachment = open("/home/pi/Fotos", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

# Send the email via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(me,password)
s.sendmail(me, family, msg.as_string())
s.quit()
