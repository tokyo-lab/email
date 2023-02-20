import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

port = 1025
smtp_server = "localhost"
sender_email = "nymhooman@gmail.com"
receiver_email = "michael.mena.g@gmail.com"
password = str(os.environ.get("password"))
subject = "test emai from python"
message = """
This message is sent from Python.
"""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, receiver_email, message)
print("Email has been sent to", receiver_email)
