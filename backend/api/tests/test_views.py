from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


factory = APIClient()


class SendMailViewTestCase(TestCase):
    def test_post_is_200(self):
        data = {'title': 'test_title', 'body': 'test_body', 'category': 1}
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 200)
