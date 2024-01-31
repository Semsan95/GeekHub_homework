import threading
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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
        filter_hidden = True
    else:
        products = Product.objects.filter(category_id=category_id)
        filter_hidden = False
    categories = Category.objects.all()
    return render(request, "products/search.html", {
            'products': products, 
            'categories': categories,
            'filter_hidden': filter_hidden
            })


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/details.html", {'product': product})


def imported(request):
    products = Product.objects.all()
    return render(request, "products/imported.html", {'products': products})


def edit(request, product_id):
    if not request.user.is_staff:
        messages.success(request, 'Ви не маєте права доступу до цієї сторінки')
        return redirect('products:search')
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
def confirm_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/confirm_delete.html', {'product': product})

@login_required
def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успішно видалено.')
        return redirect('products:search')
    else:
        return redirect('products:confirm_delete', product_id=product.id)

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
