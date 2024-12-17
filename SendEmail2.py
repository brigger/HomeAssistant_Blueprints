import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(messageText, subject):
    # Email setup (replace these with your actual details)
    sender_address = 'test.brigger@gmail.com'
    sender_pass = 'kspw ijqs wopp qmkx'
    receiver_address = 'patrick@getabstract.com'
    
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject  # Set the subject here
    
    # The body and the attachments for the mail
    message.attach(MIMEText(messageText, 'plain'))
    
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use your email provider's SMTP server
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


def main():
    # Example usage
    sendEmail("This is the message body.", "This is the subject")
    

if __name__ == "__main__":
    main()

