from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login, authenticate
# from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import SignupForm

User = get_user_model()


# # using HttpResponse
# def signup():
#     return HttpResponse('I am the Sign Up page!')
#
#
# # using render
# def contact(request):
#     context = {'message': 'I am the contact page'}
#     return render(request, 'account/contact.html', context=context)

class SignupView(FormView):
    template_name = 'account/signup.html'
    form_class = SignupForm

    def post(self, request, *args, **kwargs):
        # sign up user
        username = self.request.POST.get('username')
        password = self.request.POST.get('password1')
        password2 = self.request.POST.get('password2')

        # If the password fields don't match send the user back
        if password != password2:
            return HttpResponseRedirect(reverse('account:signup'))

        # If the username already exists, send the user back
        user = User.objects.filter(username=username)

        if user.count() > 0:
            return HttpResponseRedirect(reverse('account:signup'))

        # save user database record using fancy hashing on password
        User.objects.create_user(username=username, password=password)

        # Authenticate the user checks provided password against the hash
        user = authenticate(username=username, password=password)

        # Login the user (does the session table/cookie stuff)
        login(self.request, user)

        return HttpResponseRedirect(reverse('chat:chat'))
