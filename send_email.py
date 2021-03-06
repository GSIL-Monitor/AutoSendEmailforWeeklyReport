#!/user/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr


def send_email(from_addr, password, smtp_server, to_addr, email_content, email_header):
	# 输入Email地址和口令:
	# from_addr = 'chenjiefeng@forcegames.cn'
	# password = ''
	# 输入SMTP服务器地址:
	# smtp_server = 'smtp.exmail.qq.com'
	# 输入收件人地址：
	# to_addr = ['chenjiefeng@forcegames.cn']

	# 邮件对象:
	msg = MIMEMultipart('alternative')                 # 指定subtype为alternative，可以组合html和plain
	# 发件人昵称
	msg['From'] = '%s <%s>' % (from_addr, from_addr)
	# 收件人昵称
	msg['To'] = ','.join(x for x in to_addr)
	# 邮件主题
	msg['Subject'] = Header(email_header)

	# 邮件正文
	# msg.attach(MIMEText(email_content,'plain','utf-8'))   # 当客户端设备无法查看html，可以自动降级为纯文本
	msg.attach(MIMEText(email_content, 'html', 'utf-8'))
	#msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
	#'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
	#'<p><img src="cid:0"></p>' +    # 引用附件图片作为正文内容，编号对应Content-ID和X-Attachment-Id
	#'</body></html>', 'html', 'utf-8'))

	# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
	#with open('/root/scripts/code.jpg', 'rb') as f:
		# 设置附件的MIME和文件名，这里是png类型:
	#    mime = MIMEBase('image', 'png', filename='test.png')
		# 加上必要的头信息:
	#    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
	#    mime.add_header('Content-ID', '<0>')
	#    mime.add_header('X-Attachment-Id', '0')                         # 附件编号
		# 把附件的内容读进来:
	#    mime.set_payload(f.read())
		# 用Base64编码:
	#    encoders.encode_base64(mime)
		# 添加到MIMEMultipart:
	#    msg.attach(mime)

	# 明文方式
	#server = smtplib.SMTP(smtp_server, 25)
	# SSL加密方式
	smtp_port = 465
	server = smtplib.SMTP_SSL(smtp_server, smtp_port)
	# TLS加密方式
	#smtp_port = 587
	#server = smtplib.SMTP(smtp_server, smtp_port)
	#server.starttls()
	# 打印出和SMTP服务器交互的所有信息
	# server.set_debuglevel(1)
	
	server.login(from_addr, password)
	server.sendmail(from_addr, to_addr, msg.as_string())
	server.quit()
	
if __name__ == '__main__':
	# 输入Email地址和口令:
	from_addr = 'chenjiefeng@forcegames.cn'
	password = 'Trxi900802'
	# 输入SMTP服务器地址:
	smtp_server = 'smtp.exmail.qq.com'
	# 输入收件人地址：
	to_addr = ['chenjiefeng@forcegames.cn']
	# 邮件主题
	email_header = '周报'
	# 邮件正文
	email_content = 'test'
	
	send_email(from_addr, password, smtp_server, to_addr, email_content, email_header)