"""
Module sends the mail as a helper for the node spawn process
"""

# path module
from pathlib import Path

# SMTP server essentials
from email.message import EmailMessage
import smtplib
import ssl

# Configuration section
import sys
import os
import dotenv

try:

    env_path = os.path.join(Path.cwd(), "custom", "config.env")
    dotenv.load_dotenv(dotenv_path=env_path)

    OrgMail = os.getenv("mailID")
    OrgPass = os.getenv("password")


    port = os.getenv("mailPort")
    FROM_MAIL = OrgMail
    TO_MAIL = sys.argv[2]
    OTP = sys.argv[3]
    COMPANY_NAME = sys.argv[4]
    
    # Create the HTML file
    HTML = ""

    with open(os.path.join(Path.cwd(), "custom", "index.html"), "r", encoding="utf-8") as template:
        for LINE in template:
            REGEX = r"({.*})"

            # Checking the presence of the OTP
            if "{OTP}" in LINE:
                LINE = LINE.replace("{OTP}", OTP)

            # Checking the presence of the company name
            if "{COMPANY_NAME}" in LINE:
                LINE = LINE.replace("{COMPANY_NAME}", COMPANY_NAME)
            
            HTML += LINE
            
    message = EmailMessage()
    message['Subject'] = f"OTP for password reset"
    message['From'] = FROM_MAIL
    message['To'] = TO_MAIL
    # message.add_alternative(HTML, subtype='html')
    message.set_content(HTML, subtype='html')
    
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)
        server.login(OrgMail, OrgPass)
        server.send_message(message)
        server.quit()
        print("PYTHON SERVER :: success sent mail")
    except Exception as error:
        print(error)
        print("PYTHON SERVER :: Server error -> Mailing section")
    finally:
        sys.exit(0)
except Exception as error:
    print(error)
    print("Server error cannot send mail : section main")

