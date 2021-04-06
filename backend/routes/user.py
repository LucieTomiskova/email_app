from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from backend.database import insert_user
from services.email_sender import send_email

templates = Jinja2Templates(directory=Path(__file__).parents[2] / 'templates')

router = APIRouter()


@router.route('/registration', methods=['POST', 'GET'])
async def registration(request: Request):
    """Function for registering new user with the form.

    After registering user data are inserted into the MongoDB and confirmation email is sent.
    """
    if request.method == 'POST':
        form_data = await request.form()
        new_user = {
            'first_name': form_data.get('first-name'),
            'last_name': form_data.get('last-name'),
            'email_address': form_data.get('email-address'),
            'password': form_data.get('password')
        }
        await insert_user(new_user)
        send_email(form_data.get('email-address'))  # sends automatic email about registration

        return templates.TemplateResponse('success.html', context={'request': request})
