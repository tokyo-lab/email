import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

port = str(os.environ.get("port"))
smtp_server = str(os.environ.get("smtp_server"))
sender_email = str(os.environ.get("sender_email"))
receiver_email = str(os.environ.get("receiver_email"))
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
