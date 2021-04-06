import logging

import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from backend.config import settings
from backend.models.user import ErrorResponseModel


def send_email(to_email: str):
    """Main function for sending email from different services when one is down.
    Priority is following:
    1. Sendgrid service
    2. MailGun service

    :param to_email: recipient's email address
    """
    subject = 'Registration was successful'
    email_text = '<strong>Your registration was successful!</strong>'

    # try execute SendGrid email service
    try:
        _send_by_sendgrid(to_email, subject, email_text)
        return
    except Exception as e:
        logging.error(type(e).__name__, str(e))

    # when Sendgrid fails try to execute MailGun email service
    try:
        _send_by_mailgun(to_email, subject, email_text)
    except Exception as e:
        logging.error("Email could not be sent. Error occured by both emailing services.")
        return Exception(type(e).__name__, str(e))


def _send_by_sendgrid(to_email: str, subject: str, email_text: str):
    """Function for sending email through SendGrid provider.

    :param to_email: recipient's email address
    :param subject: subject of the sending email
    :param email_text: text of the sending email
    """
    message = Mail(from_email=settings.mail_default_sender,
                   to_emails=to_email,
                   subject=subject,
                   html_content=email_text)
    sg = SendGridAPIClient(settings.sendgrid_api_key)
    sg.send(message)


def _send_by_mailgun(to_email: str, subject: str, email_text: str):
    """Function for sending email through MailGun provider.

    :param to_email: recipient's email address
    :param subject: subject of the sending email
    :param email_text: text of the sending email
    """
    requests.post(f"https://api.mailgun.net/v3/{settings.mailgun_domain_name}/messages",
                  auth=("api", settings.mailgun_api_key),
                  data={"from": settings.mail_default_sender,
                        "to": to_email,
                        "subject": subject,
                        "text": email_text})
