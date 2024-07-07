from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import HospitalDetail
# from .models import 
#Create your views here.

def home(request):
    return HttpResponse("This is Homepage")

class ViewHospital(ListView):
    model = HospitalDetail
    template_name = "HospitalsApp/hospitals_list.html"
    context_object_name = "hospitals"

class Single_ViewHospital(DetailView):
    model = HospitalDetail
    template_name = "HospitalsApp/single_hospital.html"
    context_object_name = "hospital" 

class CreateHospital(CreateView):
    model = HospitalDetail
    template_name = "HospitalsApp/add_hospital.html"
    fields = ["name","email","contact","website","country","state","district","address","pin","latitude","longitude"]
    success_url = reverse_lazy("viewHospital")

class UpdateHospital(UpdateView):
    model = HospitalDetail
    template_name = "HospitalsApp/add_Hospital.html"
    fields = ["name","email","contact","website","country","state","district","address","pin","latitude","longitude"]
    success_url = reverse_lazy("viewHospital")

class DeleteHospital(DeleteView):
    model = HospitalDetail
    template_name = "HospitalsApp/delete_hospital.html"
    context_object_name = "hospital"
    success_url = reverse_lazy("viewHospital")