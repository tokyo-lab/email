import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.protonmail.com"
sender_email = "sonicstash@protonmail.com"
receiver_email = "michael.mena.g@gmail.com"
password = "JDQ3bsT1!h6$fsre!nwk"
subject = "test emai from python"
message = """
This message is sent from Python.
"""

context = ssl.create_default_context()


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
