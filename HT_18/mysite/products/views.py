import threading
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Product

def search(request):
    return render(request, "products/search.html")

def cart(request):
    products = Product.objects.all()
    return render(request, "products/cart.html", {'products': products})

def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/details.html", {'product': product})

@require_POST
@csrf_exempt
def fetch(request):
    product_ids = request.POST.get('product_ids', '')
    threading.Thread(
        target=Product.fetch_list,
        args=(product_ids,),
        daemon=True
    ).start()
    return render(request, "products/search.html", {'search_started': True})