from django.urls import path
from .views import SendMailView


urlpatterns = [
    path('sendmail/', SendMailView.as_view(), name='sendmail')
]
