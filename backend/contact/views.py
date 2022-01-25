from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import View
from django.shortcuts import redirect

from .models import MailerSettings, Category
from .forms import ConfigureForm, EditorFormCategory


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


class EditorView(CreateView):
    template_name = "contact/editor.html"
    form_class = EditorFormCategory
    success_url = "/contact/editor"
    template_name_suffix = 'None'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditorView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class EditorCategoryDeleteView(View):
    def get(self, request, *args, **kwargs):
        Category.objects.get(pk=self.kwargs['pk']).delete()
        return redirect('edit')
