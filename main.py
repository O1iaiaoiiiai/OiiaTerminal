import smtplib
from email.mime.text import MIMEText

def mailcustom(addrfrom, to, subject, body):
    MAIL_SERVER = "192.168.1.100"  # Your custom server IP
    MAIL_PORT = 25  # or 465 for SSL, 25 for unencrypted
    MAIL_USER = "your-username"
    MAIL_PASSWORD = "your-password"

    msg = MIMEText("Email body")
    msg['Subject'] = "Test Email"
    msg['From'] = "sender@yourdomain.com"
    msg['To'] = "recipient@example.com"

    # Connect to custom mail server (TLS)
    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
        server.starttls()  # Upgrade to encrypted connection
        server.login(MAIL_USER, MAIL_PASSWORD)
        server.send_message(msg)
        print("Email sent via custom server!")

def mailgmail(address, password, subject, body, to_address):
    # Gmail SMTP settings
    GMAIL_ADDRESS = address
    GMAIL_PASSWORD = password  # Use App Password, not regular password

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = address
    msg['To'] = to_address

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        print("Preview will be listed below.")
        print(f"Subject: {subject}")
        print(f"From: {address}")
        print(f"To: {to_address}")
        print()
        print(f"{body}")
        if input("Send? y/n") == "Y" or "y":
            server.send_message(msg)
        else:
            print("ABORT")
print("Hey! No need for argument for they are going to be asked ")
print("But before we do begin, we have some requirements.")
print("We require you have an app password from google saved to a TXT file.")
app_password = input("Do you have one set up? If so, type it here.\nIf you do bot have an app password, please set one up and save it to a TXT file. Please name it OiiaTerminal. We will also require you setup 2FA on your gmail account.\nAPP PASSWORD >> ")
print(f"App password set to {app_password}.\nIf this is incorrect, please restart the terminal and try again.")
print("We also require a name. Please type one below.")
name = input("NAME >> ")
print("We also require an email.")
emailaddr = input("EMAIL ADDRESS (must be a @gmail.com email) >> ")
input("We will not show anymore until you confirm by hitting ENTER that your email address has SMTP on, you can look into this by setting it up through the gmail.com page. (via https://support.google.com/mail/answer/7126229)")
print("We have finished setting up for you. Enjoy your terminal, new or old user!")
def checkprompt(prompt):
    if prompt == "gmailsend":
        body = input("Send (body, required) >>")
        subj = input("Subject (Required) >>")
        to = input("To (Required) >>")
        mailgmail(emailaddr, app_password, subj, body, to)
while True:
    prompt = input(f"{name},{emailaddr}*Oiia>")
    checkprompt(prompt)