#from django.shortcuts import render
#from django.http import HttpResponse #new
from django.views.generic import TemplateView #new

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
