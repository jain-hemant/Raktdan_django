from django.urls import path
from .views import *

urlpatterns = [
    # path('',index,name="index"),
    path('userlist/',UserList.as_view(),name="UserList"),
    path('userregister/',UserRegister.as_view(), name="UserRegister")
]
