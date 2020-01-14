import email.utils
import re
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Union

ENCODING = 'utf-8'


def create_email(sender_name: str, sender_addr: str, recipient_addr: List[str],
                 subject: str, html: Union[str, None], text: Union[str, None]):
    msg = MIMEMultipart()

    sender = sender_addr if not sender_name else email.utils.formataddr(
        (Header(sender_name, ENCODING).encode(), sender_addr))

    msg['From'] = sender
    msg['To'] = email.utils.COMMASPACE.join(recipient_addr)
    msg['Subject'] = Header(subject, ENCODING)
    msg['Date'] = email.utils.formatdate()

    msg_related = MIMEMultipart('related')
    msg.attach(msg_related)

    msg_alternative = MIMEMultipart('alternative')
    msg_related.attach(msg_alternative)

    if text:
        msg_text = MIMEText(text.encode(ENCODING), 'plain', ENCODING)
        msg_alternative.attach(msg_text)

    if html:
        msg_html = MIMEText(html.encode(ENCODING), 'html', ENCODING)
        msg_alternative.attach(msg_html)

    return msg


def connect_smtp(host: str, port: int, username: str, password: str):
    conn = smtplib.SMTP_SSL(host, port)
    conn.login(username, password)

    return conn


def html_to_text(email):
    return re.sub('<[^<]+?>', '', email)
