from django.http import HttpResponse


def signup(request):
    return HttpResponse('I am the Sign Up page!')