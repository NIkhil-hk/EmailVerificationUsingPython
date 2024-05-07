import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender's email credentials
sender_email = "ajay@gmail.com"
app_password = "**************"  #get this from app passwords in your sending email

# Recipient's email address
recipient_email = "nikhil@gmail.com"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Test email from Python"

# Add body to email
body = "Hello i am nikhil from St Xavier's college. This is a test email sent from Python."
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Log in to your Gmail account
    server.login(sender_email, app_password)
    
    # Send email
    server.send_message(message)

print("Email sent successfully!")
