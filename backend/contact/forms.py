from django import forms
from .models import MailerSettings


class ConfigureForm(forms.ModelForm):
    class Meta:
        model = MailerSettings
        fields = ['EMAIL_HOST', 'EMAIL_PORT',
                  'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD']
