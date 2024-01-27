import threading
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product, Category
from services.parsers import fetch_product_list
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def search(request, category_id=None): 
    if category_id is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, "products/search.html", {
            'products': products, 
            'categories': categories
            })


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/details.html", {'product': product})


def imported(request):
    products = Product.objects.all()
    return render(request, "products/imported.html", {'products': products})

def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.brand = request.POST.get('brand')
        product.category = Category.objects.get(name=request.POST.get('category'))
        product.save()
        return HttpResponseRedirect(reverse('products:details', args=(product.id, )))
    return render(request, 'products/edit.html', {
        'product': product,
        'categories': categories
    })


@login_required
@require_POST
@csrf_exempt
def fetch(request):
    product_ids = request.POST.get('product_ids', '')
    threading.Thread(
        target=fetch_product_list,
        args=(product_ids, ),
        daemon=True
    ).start()
    messages.add_message(request, messages.INFO, 'Пошук розпочато! Результати будуть доступні найближчим часом.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('products:search')))
