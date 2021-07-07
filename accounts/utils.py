from django.contrib.auth import tokens
from django.contrib.sites.shortcuts import get_current_site
from django.http import request
from django.template.loader import render_to_string

from .tokens import confirm_email_token_generator


def send_confirmation_email(request, user):
    # https://example.com/4/AJSLJS345
    token = confirm_email_token_generator.make_token(user)
    uid = user.pk
    domain = get_current_site(request)

    subject = 'Activate your account'
    message = render_to_string('registration/account_activation_email.html', 
    {
        'user': user,
        'domain': domain,
        'uid': uid,
        'token':token

    }
    )

    user.email_user(subject, message)