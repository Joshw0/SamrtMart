from django.shortcuts import render

def product_list(req):
    return render(req,'productss/product_list.html')
