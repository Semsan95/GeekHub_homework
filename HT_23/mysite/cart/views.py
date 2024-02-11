from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from products.models import Product


@login_required
def cart_home(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=[int(k) for k in cart.keys()])
    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]['quantity']
        cart_items.append({
            'product': product,
            'quantity': quantity,
        })
    return render(request, "cart/cart.html", {'cart_items': cart_items})


@login_required
def add(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    product_id = str(product_id)
    if product_id in request.session['cart']:
        request.session['cart'][product_id]['quantity'] += 1
    else:
        request.session['cart'][product_id] = {'quantity': 1}

    request.session.modified = True
    return JsonResponse({'status': 'ok'})


@login_required
def increase(request, product_id):
    product_id = str(product_id)
    request.session['cart'][product_id]['quantity'] += 1
    request.session.modified = True
    new_quantity = request.session['cart'][product_id]['quantity']
    product_price = Product.objects.get(id=product_id).price
    return JsonResponse({'status': 'ok', 'new_quantity': new_quantity, 'product_price': product_price})


@login_required
def decrease(request, product_id):
    product_id = str(product_id)
    if request.session['cart'][product_id]['quantity'] > 1:
        request.session['cart'][product_id]['quantity'] -= 1
    request.session.modified = True
    new_quantity = request.session['cart'][product_id]['quantity']
    product_price = Product.objects.get(id=product_id).price
    return JsonResponse({'status': 'ok', 'new_quantity': new_quantity, 'product_price': product_price})


@login_required
def remove(request, product_id):
    product_id = str(product_id)
    del request.session['cart'][product_id]
    request.session.modified = True
    return JsonResponse({'status': 'ok'})


@login_required
def clear(request):
    request.session['cart'] = {}
    request.session.modified = True
    return JsonResponse({'status': 'ok'})