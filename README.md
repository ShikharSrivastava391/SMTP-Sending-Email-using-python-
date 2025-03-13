# SMTP-Sending-Email-using-python
This project is a Python-based SMTP email sender that allows users to send emails using Gmail's/Outlook SMTP server. It supports both plain text and HTML emails and includes error logging using a custom logger.

Features:
✅ Send emails with both plain text and HTML formats.
✅ Uses Google App Passwords for secure authentication.
✅ Supports subject customization and email templates.
✅ Logs errors and email status using a custom logger.

Step 1: Enable SMTP Access in Gmail
Go to Your Google Account
Open Google My Account.
Enable 2-Step Verification (Mandatory for App Passwords)
Click on Security from the left menu.
Scroll to "How you sign in to Google" → 2-Step Verification → Turn it ON.
Follow the on-screen steps to verify your identity.

Step 2: Generate an App Password - [https://myaccount.google.com/apppasswords]
Under "Select app", GIVE ANY NAME TO APP.
Under "Select device", choose Windows Computer (or your preferred option).
Click "Generate".

Step 3 : Copy the password and paste it to env 
.env example :
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SENDER_EMAIL=xxxx@gmail.com(email from where you generated password)
EMAIL_PASSWORD=abcdefghijklmnop (Google will show you a 16-character password (e.g., abcd efgh ijkl mnop).)

Same thing do it for Outlook

