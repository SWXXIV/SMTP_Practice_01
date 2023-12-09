import smtplib
from variables import from_address, to_address, from_address_pass

my_email = from_address

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=from_address_pass)
connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Hello")
connection.close()