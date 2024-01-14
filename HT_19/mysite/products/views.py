import threading

from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product


def search(request):
    search_started = request.GET.get('search_started', False)
    return render(
        request, "products/search.html", {'search_started': search_started}
    )


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    product_id = str(product_id)
    if product_id in request.session['cart']:
        request.session['cart'][product_id]['quantity'] += 1
    else:
        request.session['cart'][product_id] = {'quantity': 1}

    request.session.modified = True
    return HttpResponseRedirect(reverse('imported'))


def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=[int(k) for k in cart.keys()])
    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]['quantity']
        cart_items.append({
            'product': product,
            'quantity': quantity,
        })
    return render(request, "products/cart.html", {'cart_items': cart_items})


def imported(request):
    products = Product.objects.all()
    return render(request, "products/imported.html", {'products': products})


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
    return HttpResponseRedirect(f"{reverse('search')}?search_started=True")


def cart_add_button(request, product_id):
    product_id = str(product_id)
    request.session['cart'][product_id]['quantity'] += 1
    request.session.modified = True
    return HttpResponseRedirect(reverse('cart'))


def cart_subtract_button(request, product_id):
    product_id = str(product_id)
    if request.session['cart'][product_id]['quantity'] > 1:
        request.session['cart'][product_id]['quantity'] -= 1
    request.session.modified = True
    return HttpResponseRedirect(reverse('cart'))


def cart_remove_button(request, product_id):
    product_id = str(product_id)
    del request.session['cart'][product_id]
    request.session.modified = True
    return HttpResponseRedirect(reverse('cart'))


def cart_clear_button(request):
    request.session['cart'] = {}
    request.session.modified = True
    return HttpResponseRedirect(reverse('cart'))