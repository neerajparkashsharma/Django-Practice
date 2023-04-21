from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def home(request):
    template = loader.get_template(template_name='home.html')
    context = {
        'title': 'Home',
        'heading': 'Welcome to Baham',
    }
    return HttpResponse (template.render(context,request=request))

def about(request):
    context = {
        'title': 'About Us',
        'heading': 'Welcome to Baham',
    }
    template = loader.get_template(template_name='about.html')
    return HttpResponse (template.render(context,request=request))


