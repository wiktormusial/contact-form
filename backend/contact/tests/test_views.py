from django.test import TestCase
from django.urls import reverse
from contact.models import MailerSettings


class ViewsTestCase(TestCase):
    def test_view_uses_correct_template_with_configured_settings(self):
        MailerSettings.objects.create(EMAIL_HOST="test_host",
                                      EMAIL_PORT=547,
                                      EMAIL_HOST_USER="wikt@gmail.com",
                                      EMAIL_HOST_PASSWORD="123")
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'contact/index.html')

    def test_index_view_redirect_to_configure(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('configure'))
