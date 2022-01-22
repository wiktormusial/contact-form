from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from contact.models import Category

factory = APIClient()


class SendMailViewTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title="test_cat")

    def test_post_is_201(self):
        cat = Category.objects.get(title="test_cat")
        data = {
            "title": "test_title",
            "body": "test_bod",
            "author":  "test@email.com",
            "category": cat.id
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 201)

    def test_can_not_post_without_body(self):
        cat = Category.objects.get(title="test_cat")
        data = {
            "title": "test_title",
            "author":  "test@email.com",
            "category": cat.id
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 400)

    def test_can_not_post_without_title(self):
        cat = Category.objects.get(title="test_cat")
        data = {
            "body": "test_bod",
            "author":  "test@email.com",
            "category": cat.id
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 400)

    def test_can_not_post_without_category(self):
        data = {
            "title": "test_title",
            "body": "test_bod",
            "author":  "test@email.com",
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 400)

    def test_can_not_post_with_wrong_category(self):
        data = {
            "title": "test_title",
            "body": "test_bod",
            "author":  "test@email.com",
            "category": 45
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 400)

    def test_can_not_post_without_author(self):
        cat = Category.objects.get(title="test_cat")
        data = {
            "title": "test_title",
            "body": "test_bod",
            "category": cat.id
        }
        request = factory.post(reverse('sendmail'), data, format='json')
        self.assertEqual(request.status_code, 400)
