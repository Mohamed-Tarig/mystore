from django.urls import path, include
from .views import activate_email, signup

urlpatterns = [
path('accounts/signup', signup, name="signup"),
# path('accounts/login', signup, name="login"),
# path('accounts/logout', signup, name="logout"),
path('accounts/', include('django.contrib.auth.urls')),
path('activate/<uid>/<token>/', activate_email, name="activate_email"),
]