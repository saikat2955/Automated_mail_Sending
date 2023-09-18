import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server,smtp_port,smtp_username,smtp_password,from_email,to_email,subject,body):
    #smtp_server = 'server_name'
    #smtp_port = 'port'
    #smtp_username = 'username'
    #smtp_password = 'password'

    from_email = 'example@mail.com'
    to_email = 'emaple_to@mail.com'

    subject = 'Subject'
    body = 'This is the body'
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = None  
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_username, smtp_password)

        server.sendmail(from_email, to_email, message.as_string())
        print('Email sent successfully')

    except Exception as e:
        print(f'Error: {str(e)}')

    finally:
        if server:
            server.quit()

# Call the function to send the email
send_email(smtp_server,smtp_port,smtp_username,smtp_password,from_email,to_email,subject,body)
