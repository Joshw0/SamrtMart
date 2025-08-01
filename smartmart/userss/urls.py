from django.urls import path
from . import views

app_name = 'userss'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_products/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),  
]
