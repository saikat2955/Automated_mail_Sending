# Automated_mail_Sending
 The provided code is a Python script that sends an email using the smtplib library, which is a built-in module for sending emails via the Simple Mail Transfer Protocol (SMTP)
Importing Necessary Libraries:

import smtplib: This statement imports the smtplib library, which allows us to connect to an SMTP server and send emails.
from email.mime.multipart import MIMEMultipart: This line imports the MIMEMultipart class from the email.mime.multipart module. It's used to create a multipart email message.
from email.mime.text import MIMEText: This line imports the MIMEText class from the email.mime.text module, which is used to create the text part of the email.
SMTP Server and Email Configuration:

smtp_server, smtp_port, smtp_username, and smtp_password: These variables store the SMTP server settings, including the server address, port, username, and password.
from_email and to_email: These variables store the sender's and recipient's email addresses.
subject and body: These variables store the subject and body of the email.
message: This variable is used to create a MIME multipart message and set the sender, recipient, subject, and body.
SMTP Connection:

server = None: Initializes the server variable to None.
Inside a try block, the code establishes a connection to the SMTP server using the provided server address and port. It then starts a TLS (Transport Layer Security) encryption session and logs in with the provided username and password.
Sending the Email:

The script sends the email using the server.sendmail() method, specifying the sender's email address, the recipient's email address, and the message in the form of a string.
Error Handling:

Inside the try block, exceptions are caught using a generic Exception to handle any potential errors during the SMTP connection or email sending process.
If an error occurs, it is printed to the console with the print function.
Closing the SMTP Connection:

The finally block ensures that the SMTP server connection is properly closed, regardless of whether the email was sent successfully or an error occurred.
Calling the send_email Function:

The send_email() function is called at the end of the script to initiate the email sending process.
Overall, this code sends an email with a specified subject and body from a sender's email address to a recipient's email address using the provided SMTP server settings. It includes error handling to handle exceptions that may occur during the process and ensures that the SMTP connection is closed properly.
