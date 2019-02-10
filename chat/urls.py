from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path('', views.ChatIndex.as_view(), name='chat'),
]
