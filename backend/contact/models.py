from django.db import models


class MailerSettings(models.Model):
    EMAIL_HOST = models.CharField(max_length=128)
    EMAIL_PORT = models.IntegerField()
    EMAIL_HOST_USER = models.EmailField(max_length=254)
    EMAIL_HOST_PASSWORD = models.CharField(max_length=254)

    def __str__(self):
        return self.EMAIL_HOST

    def save(self, *args, **kwargs):
        if not self.pk and MailerSettings.objects.exists():
            pass
        else:
            return super(MailerSettings, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
