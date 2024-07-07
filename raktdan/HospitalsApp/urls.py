from django.urls import path
from .views import ViewHospital,CreateHospital

urlpatterns = [
    path("",ViewHospital.as_view(),name="viewHospital"),
    path("create/",CreateHospital.as_view(),name = "createHospital")
    
]
