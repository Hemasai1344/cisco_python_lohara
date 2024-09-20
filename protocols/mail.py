import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'hemasaithaninki@gmail.com'
email_passwd = 'lmvs liew cshw ixdi'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Good morning sir!")
connection.close()
print('Mail sent successfully')