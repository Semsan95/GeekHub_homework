import threading
# A010318153, 00999030000P, A102532127, A028730069
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product, Category
from services.parsers import fetch_product_list
from django.contrib.auth.decorators import login_required


def search(request, category_id=None):
    if category_id is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    notification = request.session.pop('notification', None)
    return render(
        request, "products/search.html", {'notification': notification, 'products': products, 'categories': categories}
    )


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    notification = request.session.pop('notification', None)
    return render(request, "products/details.html", {'product': product, 'notification': notification})


def imported(request):
    products = Product.objects.all()
    return render(request, "products/imported.html", {'products': products})


@login_required
@require_POST
@csrf_exempt
def fetch(request):
    product_ids = request.POST.get('product_ids', '')
    threading.Thread(
        target=fetch_product_list,
        args=(product_ids, Product),
        daemon=True
    ).start()
    request.session['notification'] = 'Пошук розпочато! Результати будуть доступні найближчим часом.'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('products:search')))
