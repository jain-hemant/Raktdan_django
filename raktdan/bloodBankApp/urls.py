from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.bb_home.as_view(), name="bbHome"),
]

