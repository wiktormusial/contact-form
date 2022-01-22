from django.test import TestCase
from contact.models import MailerSettings
from contact.models import Category


class MailerSettingsTestCase(TestCase):
    def setUp(self):
        MailerSettings.objects.create(EMAIL_HOST="smtp.test.com",
                                      EMAIL_PORT=587,
                                      EMAIL_HOST_USER="me@test.com",
                                      EMAIL_HOST_PASSWORD='password')

        MailerSettings.objects.create(EMAIL_HOST="smtp.test.pl",
                                      EMAIL_PORT=587,
                                      EMAIL_HOST_USER="me@test.com",
                                      EMAIL_HOST_PASSWORD='password')

    def test_mail_settings_have_title(self):
        obj1 = MailerSettings.objects.get(EMAIL_HOST="smtp.test.com")
        self.assertEqual(obj1.__str__(), "smtp.test.com")

    def test_mail_settings_have_values(self):
        obj1 = MailerSettings.objects.get(EMAIL_HOST="smtp.test.com")
        self.assertEqual(obj1.EMAIL_HOST, "smtp.test.com")
        self.assertEqual(obj1.EMAIL_PORT, 587)
        self.assertEqual(obj1.EMAIL_HOST_USER, "me@test.com")
        self.assertEqual(obj1.EMAIL_HOST_PASSWORD, "password")

    def test_do_not_allow_to_create_2_objects(self):
        self.assertEqual(MailerSettings.objects.count(), 1)


class CategoriesTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title="Test category 1")
        Category.objects.create(title="Test category 2")
        Category.objects.create(title="Test category 3")

    def test_category_have_title(self):
        obj = Category.objects.get(title="Test category 1")
        self.assertEqual(obj.__str__(), "Test category 1")

    def test_can_add_many_categories(self):
        self.assertEqual(Category.objects.count(), 3)
