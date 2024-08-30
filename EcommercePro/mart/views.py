
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Simulate a product list (can also be loaded from a CSV)
PRODUCTS = [
    {'id': 1, 'name': 'Product 1', 'price': 10},
    {'id': 2, 'name': 'Product 2', 'price': 20},
    {'id': 3, 'name': 'Product 3', 'price': 30},
]

def index(request):
    products = {"glasses":550, "t-shirt":700}
    if request.method == 'POST':
        selected_items = request.POST.getlist("options")
        print(selected_items)
        base_url = "/show/"
        query_string = urlencode({"options": selected_items})
        url = f"{base_url}?{query_string}"
        return redirect(url)
    
    return render(request, 'mart/index.html', {"products_dict": products})


def mart(request):
    context = {'products': PRODUCTS}
    return render(request, 'mart/mart.html', context)

def cart(request):
    cart_products = []
    if request.method == 'POST':
        product_ids = request.POST.getlist('product')
        cart_products = [p for p in PRODUCTS if str(p['id']) in product_ids]
    context = {'cart_products': cart_products}
    return render(request, 'mart/cart.html', context)
