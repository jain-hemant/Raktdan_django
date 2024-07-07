from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class bb_home(TemplateView):
    template_name = "bbHome.html"
# Create your views here.
# class bb_home(request):
#     return render(request, 'bbHome.html', context=None)


