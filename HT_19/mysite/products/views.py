import threading

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Product
from services.parsers import fetch_product_list


def search(request):
    search_started = request.GET.get('search_started', False)
    return render(
        request, "products/search.html", {'search_started': search_started}
    )


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/details.html", {'product': product})


def imported(request):
    products = Product.objects.all()
    return render(request, "products/imported.html", {'products': products})


@require_POST
@csrf_exempt
def fetch(request):
    product_ids = request.POST.get('product_ids', '')
    threading.Thread(
        target=fetch_product_list,
        args=(product_ids, Product),
        daemon=True
    ).start()
    return HttpResponseRedirect(f"{reverse('products:search')}?search_started=True")