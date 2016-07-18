import smtplib
from email.mime.text import MIMEText


def sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('mail.ahsss.com.cn', 25)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print('[+] Strating Encrypted Session.')
        smtpServer.starttls()
        smtpServer.ehlo()
        print('[+] Logging Into Mail Server.')
        smtpServer.login(user, pwd)
        print('[+] Sending Mail.')
        smtpServer.sendmail(user,to,msg.as_string())
        print('[+] Mail sent Successfully.')
    except:
        print('[-] Sending Mail Failed.')

def main():
    user = 'shigm@ahsss.com.cn'
    pwd = '123,./Abc'
    sendMail(user, pwd, '530387905@qq.com', 'Re: Important', 'Test Message')

if __name__ == '__main__':
    main()