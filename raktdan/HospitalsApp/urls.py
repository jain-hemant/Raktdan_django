from django.urls import path
from .views import ViewHospital,CreateHospital,Single_ViewHospital,DeleteHospital,UpdateHospital

urlpatterns = [
    path("",ViewHospital.as_view(),name="viewHospital"),
    path("create/",CreateHospital.as_view(),name = "createHospital"),
    path("single_hospital/<int:pk>/",Single_ViewHospital.as_view(),name="singleHospital"),
    path("update_hospital/<int:pk>/",UpdateHospital.as_view(),name="updateHospital"),
    path("delete_hospital/<int:pk>/",DeleteHospital.as_view(),name="deleteHospital")
    
]
