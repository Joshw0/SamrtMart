from django.urls import path
from .import views

app_name = 'userss'

urlpatterns = [
    path('',views.home,name='home')
]