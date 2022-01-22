import smtplib
from email.message import EmailMessage


class MailSender:

    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def show_data(self):
        print(self.server)
        print(self.port)
        print(self.username)
        print(self.password)

    def server_connect(self):
        server = smtplib.SMTP_SSL(self.server, self.port)
        server.login(user=self.username,
                     password=self.password)

        return server

    def write(self, title, recipient, content):
        msg = EmailMessage()
        msg['Subject'] = title
        msg['To'] = recipient
        msg.set_content(content)
        self.server_connect().send_message(msg)

        return True
