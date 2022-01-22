from rest_framework import serializers
from contact.models import MailerSettings
from contact.models import Category
from utils.mailsender import mailsender


class SendMailSerializer(serializers.Serializer):
    author = serializers.EmailField()
    title = serializers.CharField(max_length=300)
    body = serializers.CharField()
    category = serializers.IntegerField()

    def validate_category(self, value):
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError('invalid category')
        return value

    def create(self, validated_data):
        settings = MailerSettings.objects.all().first()
        mailer = mailsender.MailSender(settings.EMAIL_HOST, settings.EMAIL_PORT,
                                       settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        title = validated_data['title']
        body = validated_data['body']
        author = validated_data['author']
        category = validated_data['category']
        msg_title = f'[{category}]: {title}'
        msg_content = f'{author} send: \n{body}'

        mailer.write(msg_title, author, msg_content)
        return validated_data
