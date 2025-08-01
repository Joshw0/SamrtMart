from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, Category
def home(req):
    return render(req, 'home/home.html')


def add_product(request):
    if request.method == 'POST':

        name = request.POST['name']
        image = request.FILES.get('image')
        price = request.POST['price']
        discount_price = request.POST.get('discount_price') or None
        description = request.POST.get('description')
        stock = request.POST['stock']
        is_available = 'is_available' in request.POST


        Product.objects.create(
            
            name=name,
            image=image,
            price=price,
            discount_price=discount_price,
            description=description,
            stock=stock,
            is_available=is_available
        )
        return redirect('products:product_list')  # Change to your product list URL name

    categories = Category.objects.all()
    return render(request, 'adminn/product_add.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('userss:add_category')  # Reload the form after adding
    return render(request, 'adminn/product_add.html')