from django.urls import path

from . import views

urlpatterns = [
    # path('<urlPattern>', views.<viewFunction>, name = '<path_reference_name>'),
    # path('<urlPattern>', views.<ClassBasedView>.as_view(), name= '<path_reference_name>')
    path('', views.home, name = 'homepage'),
    path('about', views.aboutview, name = 'aboutpage'),
    path('products/<int:pk>', views.productDetails.as_view(), name = 'prod_details'),
    path('products/add', views.AddProduct.as_view(), name='add_product'),
    path('products/edit/<int:pk>', views.EditProduct.as_view(), name = 'Edit_product'),
    path('products/edit/<int:pk>', views.DeleteProduct.as_view(), name = 'delete_product'),
    
]