import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()  # access .env file


class Settings(BaseSettings):
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    mailgun_api_key = os.getenv('MAILGUN_API_KEY')
    mailgun_domain_name = os.getenv('MAILGUN_DOMAIN_NAME')
    mail_default_sender = os.getenv('EMAIL_SENDER')


settings = Settings()
