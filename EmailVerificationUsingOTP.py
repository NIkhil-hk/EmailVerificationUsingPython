import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender's email credentials
sender_email = "ajay@gmail.com"
app_password = "*********"  # Get this password from app passwords

# Recipient's email address
print("Verify you Email to continue. ")
recipient_email = input("Enter your Email address : ")
OTP = random.randint(100000,999999) 

print("Sending OTP Please Wait...")
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "OPT Verification From Python"

# Add body to email
body = "Hello User,\nThe Verification Code is  "+str(OTP)
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Log in to your Gmail account
    server.login(sender_email, app_password)
    
    # Send email
    server.send_message(message)

print("OTP Sent \nCheck the Inbox ")

entered_OTP = int(input("Enter the OTP : "))

while True:
    if(entered_OTP==OTP):
        print("Verification Successful !!")
        print("WELCOME User ")
        break
    else:
        print("Wrong OTP Enter again")
        entered_OTP=int(input())
    
