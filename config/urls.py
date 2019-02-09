from django.contrib import admin
from django.urls import path, include


from chat import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    # path('api', include('api.urls')),
    # path('chat', include('chat.urls')),
    path('admin/', admin.site.urls),
]
