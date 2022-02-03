
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):

    fromMail = "test616161@gmail.com" #kimden gidecek?
    server = smtplib.SMTP("smtp.gmail.com",587) # host belirtiyoruz.

    server.starttls() #bir sonraki katmana gönderiyor eposta gönderebilmek için
    server.login(fromMail,616161)

    message = MIMEMultipart('alternative')
    message ['Price decreased'] = subject

    htmlContent = MIMEText(content,'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    server.quit()
