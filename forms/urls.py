from django.urls import path
from .views import FormDetail

urlpatterns = [
    path("<int:pk>/detail", FormDetail.as_view(), name="form"),
]