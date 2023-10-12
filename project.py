import smtplib
import os

email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get("EMAIL_PASS")
with smtplib.SMTP('smtp.gmail.com',587) as smtp:   #587 is port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    #ehlo is alternative to helo for services that support the smtp services extensions
    #in any case helo or ehlo is must command for the smtp clien tp commence a mail transfer


smtp.login(email_id,email_pass)

subject = 'Fight against coronavirus'  #subject which comes in email
bosy = "Hey , hi let's fight against coronavirus by staying at home"

msg = f'subject : {subject}\n\n\n{body}'
smtp.sendmail(email_id,'ankitpandeypython10@gmail.com',msg)
