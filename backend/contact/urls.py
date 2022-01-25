from django.urls import path
from .views import ContactView, ConfigureView, EditorView, EditorCategoryDeleteView

urlpatterns = [
    path('', ContactView.as_view(), name="index"),
    path('configure', ConfigureView.as_view(), name="configure"),
    path('editor', EditorView.as_view(), name="edit"),
    path('cat/<int:pk>/delete',
         EditorCategoryDeleteView.as_view(),
         name="deletecategory")
]
