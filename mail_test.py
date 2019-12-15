#coding=utf-8
import smtplib
from email.mime.text import MIMEText

def send_mail(username,passwdrd,recv,title,content,mail_host='smtp.qq.com',port=465):
    msg=MIMEText(content)
    msg['subject']=title
    msg['from']=username
    msg['to']=recv
    smtp=smtplib.SMTP_SSL(mail_host,port)
    smtp.login(username,passwdrd)
    smtp.sendmail(username,recv,msg.as_string())
    smtp.quit()
    print("发送成功")

if __name__=='__main__':
    email_user='413826955@qq.com'
    email_pwd='slbbehdhxmelcbch'
    maillist='413826955@qq.com'
    title='测试发送邮件'
    content='112390812409124'
    send_mail(email_user,email_pwd,maillist,title,content)