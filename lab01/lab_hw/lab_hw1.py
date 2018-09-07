from gmail import GMail, Message
import smtplib
import datetime
now = datetime.datetime.now()
day_week = datetime.datetime.now().weekday()

mail = GMail("c4e21.nam@gmail.com","a2811994")
body = '''<p>Gửi sếp ____,</p>
<p>S&aacute;ng nay do t&igrave;nh h&igrave;nh sức khỏe kh&ocirc;ng tốt, bị sốt nhiệt độ cao, em viết thư n&agrave;y xin ph&eacute;p nghỉ l&agrave;m ng&agrave;y h&ocirc;m nay. Em sẽ cập nhật t&igrave;nh h&igrave;nh c&ocirc;ng việc qua email.</p>
<p>Em cảm ơn,</p>
<p>Nam</p>
'''

msg = Message("Title", to="c4e21.nam@gmail.com", html=body)

if day_week == 5 and 6: #thu 7, chu nhat
    print()
else:
    if now.hour > 7:
        mail = smtplib.SMTP('localhost')
        mail.send(msg)
        print("email sent")