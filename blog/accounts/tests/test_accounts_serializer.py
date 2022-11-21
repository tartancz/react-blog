import pytest
from django.core import mail

from accounts.serializers import CustomRegisterSerializer
from django.contrib.auth.models import User

data = {
    "username": "user2001",
    "first_name": "first",
    "last_name": "last",
    "password1": "pass147word",
    "password2": "pass147word",
    "email": "user@gmail.com",
}




def test_ser_registration_email_right_url(api_client, settings):
    api_client.post("/auth/registration/", data=data)
    email = mail.outbox[0]
    assert len(mail.outbox) == 1
    assert settings.FROND_END_VERIFY_URL in email.body


def test_ser_registration_first_and_last_name(api_client):
    api_client.post("/auth/registration/", data=data)
    user = User.objects.get(username=data['username'])
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']



