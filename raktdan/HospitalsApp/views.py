from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import HospitalDetail
# from .models import 
#Create your views here.

def home(request):
    return HttpResponse("This is Homepage")

class HospitalView(ListView):
    model = HospitalDetail
    template_name = "HospitalsApp/hospitals_list.html"
    context_object_name = "Hospitals"

class CreateHospital(CreateView):
    model = HospitalDetail
    template_name = "HospitalsApp/add_hospitals.html"
    fields = ["name","state","district","address"]
    