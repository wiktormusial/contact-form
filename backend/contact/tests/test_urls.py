from django.test import TestCase
from django.test import Client
from django.urls import reverse
from contact.models import MailerSettings

c = Client()


class URLTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        MailerSettings.objects.create(EMAIL_HOST="test_host",
                                      EMAIL_PORT=547,
                                      EMAIL_HOST_USER="wikt@gmail.com",
                                      EMAIL_HOST_PASSWORD="123")
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_url_configure_exists(self):
        response = c.get(reverse('configure'))
        self.assertEqual(response.status_code, 200)
