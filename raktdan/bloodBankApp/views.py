from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class bb_home(TemplateView):
    template_name = "bbHome.html"
    

# class bb_home(request):
#     return render(request, 'bbHome.html', context=None)


