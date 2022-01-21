from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'contact/index.html')
