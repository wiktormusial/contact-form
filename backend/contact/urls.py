from django.urls import path
from .views import ContactView, ConfigureView, EditorView

urlpatterns = [
    path('', ContactView.as_view(), name="index"),
    path('configure', ConfigureView.as_view(), name="configure"),
    path('editor', EditorView.as_view(), name="edit")
]
