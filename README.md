## About

Simple application with implemented email services (SendGrid, MailGun).

Application is based on a simple form, that saves the data into MongoDB.

Application serves for registering new users. After filling all the required fields into the form all the information
is saved to MongoDB and user receives automatic confirmation email.

### User data format

```
{
   '_id': ObjectId,
   'first_name': Lucie,
   'last_name': Tomiskova,
   'email_address': lucie@mail.com,
   'password': some_password
}
```

### Create .env file
Create env file with credentials in following format:

```
MONGO_URI=<mongodb://...>
SENDGRID_API_KEY=<sendgrid_api_key>
MAILGUN_API_KEY=<mailgun_api_key>
MAILGUN_DOMAIN_NAME=<mailgun_domain_name>
EMAIL_SENDER=<sender@mail.com>
```

### Run app locally
Run in command line:
`pip install -r requirements.txt`

`uvicorn backend.app:app --reload`

### Run app with Docker
Build the image:
`docker build -t email_image .`

Create container and map the ports (I'm using host port 4400):
`docker run -d --env-file .env -- name my_email_app -p 4440:8000 email_image`