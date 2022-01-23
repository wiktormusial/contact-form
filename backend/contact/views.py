from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import MailerSettings

class ContactView(TemplateView):
    template_name = "contact/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not MailerSettings.objects.count() == 1:
            return redirect('configure')
        else:
            return self.render_to_response(context)

class ConfigureView(View):
    def get(self, request):
        return HttpResponse("test")
