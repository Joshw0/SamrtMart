from django.shortcuts import render
from userss.models import Product,Category  # Assuming the Product model is in userss app

def product_list(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    return render(request, 'productss/product_list.html', {'products': products,'categorys':categorys})