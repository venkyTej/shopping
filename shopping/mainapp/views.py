from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product

# create your views here



def home(request):
    template = loader.get_template('home.html')
    context = {
        'products' : Product.objects.all(), # HERE 'P' product is capital because product is the claas name so class name start with capithal letter.not
        'search_bar' : True 
        

    }
    return HttpResponse(template.render(context, request))

class productDetails(DetailView):
    model = Product
    template_name = 'product_details.html' 



def aboutview(request):
    template = loader.get_template('about.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


# crud operatioons-----

# create  product-----
class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields ='__all__'
    success_url ='/'


    
    # u -- update-- product----
class EditProduct(UpdateView):
    model = Product
    context_object_name = 'Product'
    template_name = 'Edit_Product.html'   
    fields = ['img', 'price', 'stock', 'desc'] 
    success_url = '/'

# d -- delete the product-----
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'


def searchView(request):
    query = request.GET.get('search_text')

    result_products = Product.objects.filter(name__icontains = query)
    context =  {
        'prods' : result_products,
        'query' : query,
        'search_bar' : True
    }

    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))