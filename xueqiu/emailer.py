__author__ = 'evan'
import smtplib
from email.mime.text import MIMEText

def send_email(message):
    '''

    :param message: message to send
    :return:bool
    '''
    me = 'test@email.com'
    you = 'yanheven@qq.com'
    msg = MIMEText(message)
    msg['Subject'] = 'Xueqiu Tranction'
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_email('test')