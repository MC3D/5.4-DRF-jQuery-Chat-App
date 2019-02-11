from django.forms import forms

from .models import MessageModel


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['text']


