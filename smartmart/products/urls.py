from django.urls import path
from .import views

app_name = 'products'

urlpatterns = [
        path('productlist/',views.product_list,name='product_list'),
]