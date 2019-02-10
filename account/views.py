from django.shortcuts import render
from django.http import HttpResponse


# using HttpResponse
def signup():
    return HttpResponse('I am the Sign Up page!')


# using render
def contact(request):
    context = {'message': 'I am the contact page'}
    return render(request, 'account/contact.html', context=context)
