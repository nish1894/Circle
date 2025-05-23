from django import forms
from django.forms import ModelForm

from apps.messenger.models import *


class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Type message here...', 'class': 'p-4 text-black', 'maxlength':'300', 'autofocus': True}),
        }
