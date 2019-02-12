from django.contrib.auth.forms import UserCreationForm #https://docs.djangoproject.com/en/2.1/topics/auth/default/#creating-users
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')