from django.http import HttpResponse


def index(requxest):
    return HttpResponse('Hello Chat App!')