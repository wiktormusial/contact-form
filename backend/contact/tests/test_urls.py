from django.test import TestCase
from django.test import Client
from django.urls import reverse

c = Client()


class URLTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_url_configure_exists(self):
        response = c.get(reverse('configure'))
        self.assertEqual(response.status_code, 200)
