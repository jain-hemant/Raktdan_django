from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import UserModel

# Create your views here.

def index(request):
    return HttpResponse("This is Index")


class UserList(ListView):
    model = UserModel
    template_name = "UserList.html"
    context_object_name = "users"

class UserRegister(CreateView):
    model = UserModel
    template_name = "UserRegister.html"
    fields = ["firstName","lastName","email","password","blood","phone","phone2","address"]
    success_url = "/users/userlist/"
        
