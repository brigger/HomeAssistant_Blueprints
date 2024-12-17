#!/usr/bin/env python3

import smtplib, ssl

def sendEmail(messageText):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "test.brigger@gmail.com"  # Enter your address
    receiver_email = "patrick@getabstract.com"  # Enter receiver address
    #password = "tE3tbRi99er771"
    password = 'kspw ijqs wopp qmkx'
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messageText)

    print('Email sent successfully!')


#Example usage
sendEmail("Email Alert sent successfully")