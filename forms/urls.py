from django.urls import path
from .views import FormDetail

urlpatterns = [
    path("", FormDetail.as_view, name="form"),
]