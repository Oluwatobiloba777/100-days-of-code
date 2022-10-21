import smtplib

from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

MAIL_PROVIDER_SMTP_ADDRESS = "YOUR EMAIL PROVIDER SMTP ADDRESS"
EMAIL_ADDRESS = "YOUR EMAIL ADDRESS"
PASSWORD = "YOUR EMAIL PASSWORD"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def sendEmail(self, emails,message,flightLink):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDRESS, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL_ADDRESS,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n {message}\n{flightLink}".encode('utf-8')
                )
