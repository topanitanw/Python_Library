
import smtplib
import socket
from email.mime.text import MIMEText

def send_email(src_email, dst_email, content):
    '''
    Send an email with a content.

    Ex
    src_email = 'hello@gmail.com'
    dst_email = 'hi@hotmail.com'
    send_email(src_email, dst_email, "what's up?")
    '''
    if not isinstance(content, str):
        content = ""

    msg = MIMEText(content)
    msg['Subject'] = 'just sey hi %s' % (socket.gethostname())
    msg['From'] =  SRC_EMAIL
    msg['To'] = DST_EMAIL

    s = smtplib.SMTP('localhost')
    s.sendmail(SRC_EMAIL, [DST_EMAIL], msg.as_string())

    s.quit()
