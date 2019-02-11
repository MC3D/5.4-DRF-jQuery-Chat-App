from rest_framework.serializers import ModelSerializer

from chat.models import Message


# This class is responsible for properly formatting our model as json
# We need to tell it the model to use, and which fields we want included in the json.
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'user', 'created', ]

