from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
        path('/message/', views.MessageView.as_view({
            'get': 'list',  # GET method should list objects
            'post': 'create'  # POST method should create object
        }), name="messages"),
]
