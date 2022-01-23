from django import forms
from django.core.exceptions import ValidationError
from utils.mailsender import mailsender
from .models import MailerSettings


class ConfigureForm(forms.ModelForm):
    class Meta:
        model = MailerSettings
        fields = ['EMAIL_HOST', 'EMAIL_PORT',
                  'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['EMAIL_HOST'].widget.attrs.update({'class': 'form-control'})
        self.fields['EMAIL_PORT'].widget.attrs.update({'class': 'form-control'})
        self.fields['EMAIL_HOST_USER'].widget.attrs.update({'class': 'form-control'})
        self.fields['EMAIL_HOST_PASSWORD'].widget.attrs.update({'class': 'form-select'})

    def clean(self):
        super().clean()
        host = self.cleaned_data.get('EMAIL_HOST')
        port = self.cleaned_data.get('EMAIL_PORT')
        user = self.cleaned_data.get('EMAIL_HOST_USER')
        passw = self.cleaned_data.get('EMAIL_HOST_PASSWORD')

        mail = mailsender.MailSender(host, port, user, passw)

        if mail.check_connection() != "Ok":
            raise ValidationError(
                "Something went wrong during authentication process, try again",
                code='connection_error')
