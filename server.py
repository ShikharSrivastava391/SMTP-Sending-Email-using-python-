import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from logger import CustomLogger
load_dotenv()
__config = {
    "EMAIL_SMTP_SERVER": os.getenv("EMAIL_SMTP_SERVER"),
    "EMAIL_PORT": int(os.getenv("EMAIL_PORT")),
    "EMAIL_SENDER_EMAIL": os.getenv("EMAIL_SENDER_EMAIL"),
    "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
}
GirikonSendMailLog = CustomLogger.get_logger("GirikonSendMail")


def get_subject(__data, subject=None):
    try:
        if subject is not None:
            return subject
        elif "error" in __data:
            return f"Error: Please check email for more details"
        else:
            return "Collection has been successfully vectorized, Now you can ask any question from your knowledge base"
    except Exception as e:
        GirikonSendMailLog.error(f"Error in get_subject Error:GSM001\t {e}")
        return "Information from Girikon.AI"


def get_template(_type, __data, html=None):
    try:
        if html is not None:
            return html
        elif "error" in __data:
            if _type == "text":
                return f"""Hello {__data["user_name"]},\n\n{__data["error"]}"""
            elif _type == "html":
                return f"""<html><head></head><body><p>Hello {__data["user_name"]},</p>
                <p>{__data["error"]}</p><p>Team Girikon.AI</p></body></html>"""
        else:
            if _type == "text":
                return f"""Hello {__data["user_name"]},\nYour model has been trained successfully. Please click on the link below to access playground:\n{__data["web_url"]}/{__data["org_name"]}/playground"""
            elif _type == "html":
                return f"""<html><head></head><body><p>Hello {__data["user_name"]},</p>
                <p> Your model has been trained successfully. Please click on the link below to access playground:</p>
                <br/><a href="{__data["web_url"]}/{__data["org_name"]}/playground">Playground</a><p>Team Girikon.AI</p></body></html>"""
    except Exception as e:
        GirikonSendMailLog.error(f"Error in get_template Error:GSM002\t {e}")
        return "Information from Girikon.AI"


def send_mail(to=None, subject=None, html=None, __data=None):
    print("inside send_email")
    try:
        print("inside try of send_mail")
        mailServer = None
        if __data is None:
            __data = {
                "email": "shikharsrivastava43648@gmail.com",
                "user_name": "User",
                "web_url": "https://playground.girikon.ai",
                "org_name": "org_name",
            }
        msg = MIMEMultipart("alternative")
        msg["Subject"] = get_subject(__data, subject)
        msg["From"] = __config["EMAIL_SENDER_EMAIL"]
        to = (
            to
            if to is not None
            else __data["email"] if "email" in __data else "shikhar.srivastava@girikon.com"
        )
        msg["To"] = to

        # print(msg.as_string().encode())
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(get_template("text", __data, html), "plain")
        part2 = MIMEText(get_template("html", __data, html), "html")

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Try to log in to server and send email
        try:
            print("inside second try block")
            # Create a secure SSL context
            context = ssl.create_default_context()
            mailServer = smtplib.SMTP(
                __config["EMAIL_SMTP_SERVER"], __config["EMAIL_PORT"]
            )
            mailServer.ehlo()  # Can be omitted
            mailServer.starttls(context=context)  # Secure the connection
            mailServer.ehlo()  # Can be omitted
            mailServer.login(__config["EMAIL_SENDER_EMAIL"], __config["EMAIL_PASSWORD"])
            # print("before send mail", __config["EMAIL_SENDER_EMAIL"])
            # print("before send mail", to)
            # print("before send mail", msg.as_string())
            # mailServer.sendmail(__config["EMAIL_SENDER_EMAIL"], "arun.baiswal@girikon.com", "This is a test email sent from Python")
            mailServer.sendmail(__config["EMAIL_SENDER_EMAIL"], to, msg.as_string())
            GirikonSendMailLog.info(f"Email sent successfully to {to}")
        except Exception as e:
            # Print any error messages to stdout
            GirikonSendMailLog.error(f"Error in send_mail Error:GSM003\t" + str(e))
        finally:
            if mailServer is not None:
                mailServer.quit()

    except Exception as e:
        print("inside catch of send_mail")
        GirikonSendMailLog.error(f"Error in send_mail Error:GSM004\t {e}")
        return None
