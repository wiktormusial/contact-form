from django.urls import path
from .views import ContactView, ConfigureView

urlpatterns = [
    path('', ContactView.as_view(), name="index"),
    path('configure', ConfigureView.as_view(), name="configure")
]
