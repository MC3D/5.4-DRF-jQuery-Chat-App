# from django.views.generic import TemplateView

from rest_framework import viewsets

from chat.models import Message
from .serializer import MessageSerializer


# class IndexView(TemplateView):
#     template_name = 'index.html'


# An alternative is to use Django Rest Framework.
# DRF lets us use a ModelViewSet that can respond to requests for json
# and send back valid responses. It will set the content type and
# generate valid json without us sweating the details.
class MessageView(viewsets.ModelViewSet):
    # We have to tell the view what data (queryset) we want to use
    # just like in our basic example
    queryset = Message.objects.all()

    # We have to tell the view what model fields we want, so
    # we do that with a serializer class.
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
