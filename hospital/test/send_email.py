import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件发送者和接收者
sender_email = "yun.helen.tao@gmail.com"
receiver_email = "Helen.Tao@ucareqld.com.au"
password = "rmax bfty alro rqeb"

# 创建 MIME 多部分消息对象
message = MIMEMultipart("alternative")
message["Subject"] = "Python SMTP Email Test"
message["From"] = sender_email
message["To"] = receiver_email

# 创建邮件正文内容
text = """\
Hi,
How are you?
This is a test email sent from Python."""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.python.org">Python</a> test email.
    </p>
  </body>
</html>
"""

# 将文本和 HTML 添加到邮件消息中
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# 创建 SMTP 连接
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # 启用安全传输模式
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
