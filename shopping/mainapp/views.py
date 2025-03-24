from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

from .models import Product

# create your views here



def home(request):
    template = loader.get_template('home.html')
    context = {
        'products' : Product.objects.all()

    }
    return HttpResponse(template.render(context, request))



def aboutview(request):
    template = loader.get_template('about.html')
    context = {

    }
    return HttpResponse(template.render(context, request))



    
    