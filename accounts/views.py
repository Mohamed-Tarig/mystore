from django import forms
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.models import User

from .forms import SignUpForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator

User = get_user_model()

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            return render(request, 'registration/signup_success.html')    


    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')