import smtplib
from email.message import EmailMessage



server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("yourbotemailservice@gmail.com", "BRRRR")

email = EmailMessage()
email['From'] = "yourbotemailservice@gmail.com"
email['To'] = "kalana1answers1history@solarunited.net"
email['Subject'] = "YourBot is working!"
email.set_content("TEST EMAIL FROM YOUR BOT TEST IG")
server.send_message(email)
server.close()