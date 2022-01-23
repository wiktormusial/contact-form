from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.shortcuts import redirect

from .models import MailerSettings
from .forms import ConfigureForm


class ContactView(TemplateView):
    template_name = "contact/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not MailerSettings.objects.count() == 1:
            return redirect('configure')
        else:
            return self.render_to_response(context)


class ConfigureView(CreateView):
    form_class = ConfigureForm
    model = MailerSettings
    template_name = "contact/configure.html"
    success_url = '/contact'

    def get(self, request, *args, **kwargs):
        if MailerSettings.objects.exists():
            return redirect('index')
        else:
            return super().get(request, *args, **kwargs)
