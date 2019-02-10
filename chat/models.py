from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#referencing-the-user-model


class Message(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=264,)
    created = models.DateTimeField(auto_now_add=True,)

    # string representation of your model so you can print out an instance if you want
    def __str__(self):
        return self.text
